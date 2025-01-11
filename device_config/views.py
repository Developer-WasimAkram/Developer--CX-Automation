from django.shortcuts import render 
from django.http import HttpResponse
from netmiko import ConnectHandler
import pandas as pd
import os
from django.conf import settings
from netmiko.ssh_autodetect import SSHDetect


def home(request):
    
    return render(request, 'home/AppPage.html')

# Create your views here
def device_config(request):
    if request.method == 'POST':
        try:
            # Get POST data
            host = str(request.POST.get('host'))
            username = str(request.POST.get('username'))
            password = str(request.POST.get('password'))
            #device_type = request.POST.get('device_type')
            file = request.FILES.get('file')

            # Validate file input
            if not file:
                raise ValueError("No file uploaded. Please upload a valid Excel file.")

            # Set up the device connection details
            device = {
                'device_type': "autodetect",  # Auto detect device type
                'host': host,
                'username': username,
                'password': password,
                'timeout': 10,
            }

            # Read the Excel file into a DataFrame
            try:
                df = pd.read_excel(file)
            except Exception as e:
                raise ValueError(f"Failed to read the Excel file: {e}")

            # Establish the connection to the device
            try:
                connection = ConnectHandler(**device)
            except Exception as e:
                raise ConnectionError(f"Failed to connect to the device: {e}")

            outputs = []

            # Loop through the commands in the DataFrame and send them to the device
            for id, row in df.iterrows():
                try:
                    command = row['Commands']
                    output = connection.send_command(str(command))
                    outputs.append(output)
                except Exception as e:
                    outputs.append(f"Error executing command {row['Commands']}: {e}")
                    continue  # Continue with the next command even if an error occurs

            # Add the outputs as a new column in the DataFrame
            df['Output'] = outputs

            # Save the DataFrame to an Excel file
            
            file_name = 'Generated_Report_file.xlsx'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            #file_path = 'command_file.xlsx'
            try:
                df.to_excel(file_path, index=False)
            except Exception as e:
                raise ValueError(f"Failed to save the Excel file: {e}")

            # Disconnect the session
            connection.disconnect()
            print(file_path)
            # Pass the file path to the template for download
            return render(request,  "config/config.html", {'file': file_path})

        except ValueError as ve:
            # Handle issues with form data or file reading
            return render(request, "config/config.html", {'error': str(ve)})

        except ConnectionError as ce:
            # Handle connection issues with the device
            return render(request, "config/config.html", {'error': str(ce)})

        except Exception as e:
            # General exception handling
            return render(request, "config/config.html", {'error': f"An unexpected error occurred: {e}"})

    # GET request handling
    return render(request, "config/config.html")




def download_file(request):
    # Define the path to the generated file
    file_name = 'Generated_Report_file.xlsx'
    file_path = os.path.join(settings.MEDIA_ROOT,file_name)
    #file_path='command_file.xlsx'
    
    #file_path = os.path.join('data', file_name)
    
    if os.path.exists(file_path):
        
        # Open the file in binary mode
        with open(file_path, 'rb') as file:
            # Set the content type and disposition for downloading
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename= "{file_name}" '# Specify download filename
            return response
    else:
        return HttpResponse("File not found.", status=404)


