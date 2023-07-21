import requests
import datetime
import pytz
import traceback
import requests


def update_status(survey_url, layer, token, payload):
    """
    Takes a prepared data payload and feature layer information and sends updates through a AGOL REST API request
    to update the "Weekly_Update_Status" field.

    If an error occurs within the connection or update process, the function will return an error log, if no error occurs,
    fucntion returns None.
    """
        
    #Set the Error Catch
    error = None
    
    try:

        #ApplyEdits URL for Survey Table
        url = f'{survey_url}/{layer}/applyEdits'

        #Create Upload Parameters
        params = {
            'f':'json',
            'token':token,
            'updates':f'{payload}'
        }

        #Initiate Update to AGOL
        response = requests.post(url, params)


        #If Response Connected
        if response.status_code == 200:

            #Create JSON Dict from Response
            response = response.json()

            #If Response Update was NOT Successfull, Create Error Log
            if response['updateResults'][0]['success'] == False:

                error = {   'Event':'Uploading Status Update Failed',
                            'OBJID': response['updateResults'][0]['uniqueId'],
                            'Code': response['updateResults'][0]['error']['code'],
                            'Details': response['updateResults'][0]['error']['description']}
                
                raise Exception(f"Failed to Upload Status to AGOL")
            
        
        #If there is a failure to connect
        elif response.status_code == 400:

            error = {   'Event': 'Failed to Connect',
                        'OBJID': '',
                        'Code': response['error']['code'],
                        'Details': response['error']['details'] }
            
            raise Exception("Failed to Connect to AGOL")
            

        #If Response Didn't Connect, Raise Exception
        else:
            error = {   'Event': 'Failed to Connect',
                        'OBJID': '',
                        'Code':'',
                        'Details': '' }
            
            raise Exception("Failed to Connect to AGOL")


    #If Exception Occurred, Return Error
    except Exception as e:
            
        return error
        




def update_points(start_points_url, start_points_layer, end_points_url, end_points_layer, token, geo_package):
    """
    Takes a prepared data payload conataining geographic information from the survey start and end points that were submitted by construction managers and
    updates the project start and end points the start and end point feature layers

    If an error occurs within the connection or update process, the function will return an error log, if no error occurs,
    fucntion returns None.
    """
    
    #Set the Error Catch
    error = None


    try:

        ############ UPDATE START POINT ##############

        #ApplyEdits URL for Start Points Table
        url = f'{start_points_url}/{start_points_layer}/applyEdits'

         #Create Upload Parameters
        params = {
            'f':'json',
            'token':token,
            'updates':f"{geo_package['starts']}"
        }

        #Initiate Update to AGOL
        response = requests.post(url, params)

        #If Response Connected
        if response.status_code == 200:

            #Create JSON Dict from Response
            response = response.json()

            #If Response Update was NOT Successfull, Create Error Log
            if response['updateResults'][0]['success'] == False:

                error = {   'Event':'Uploading Start GeoPoint Update Failed',
                            'OBJID': response['updateResults'][0]['uniqueId'],
                            'Code': response['updateResults'][0]['error']['code'],
                            'Details': response['updateResults'][0]['error']['description']}
                
                raise Exception("Failed to Upload Start Point Updated to AGOL")
            

        #If Response Didn't Connect, Raise Exception
        else:
            error = {   'Event': 'Failed to Connect',
                        'OBJID': '',
                        'Code':'',
                        'Details': '' }
            
            raise Exception("Failed to Connect to AGOL")
        


         ############ UPDATE END POINT ##############

        #ApplyEdits URL for Start Points Table
        url = f'{end_points_url}/{end_points_layer}/applyEdits'

         #Create Upload Parameters
        params = {
            'f':'json',
            'token':token,
            'updates':f"{geo_package['ends']}"
        }

        #Initiate Update to AGOL
        response = requests.post(url, params)

        #If Response Connected
        if response.status_code == 200:

            #Create JSON Dict from Response
            response = response.json()

            #If Response Update was NOT Successfull, Create Error Log
            if response['updateResults'][0]['success'] == False:

                error = {   'Event':'Uploading End GeoPoint Update Failed',
                            'OBJID': response['updateResults'][0]['uniqueId'],
                            'Code': response['updateResults'][0]['error']['code'],
                            'Details': response['updateResults'][0]['error']['description']}
                
                raise Exception("Failed to Upload End Point Update to AGOL")


        #If there is a failure to connect
        elif response.status_code == 400:

            error = {   'Event': 'Failed to Connect',
                        'OBJID': '',
                        'Code': response['error']['code'],
                        'Details': response['error']['details'] }
            
            raise Exception("Failed to Connect to AGOL")
                                

        #If Response Didn't Connect, Raise Exception
        else:

            error = {   'Event': 'Failed to Connect',
                        'OBJID': '',
                        'Code':'',
                        'Details': '' }
            
            raise Exception("Failed to Connect to AGOL")



    #If Exception Occurred, Return Error
    except Exception as e:
            
        return error
    



def update_approved(approved_url, layer, token, package):
    """
    Takes a prepared data package from Survery123 Submissions once they are approved by Michael Baker managers and shuttles the data off to
    the Approved Project Information feature layer table. 

    If an error occurs within the connection or update process, the function will return an error log, if no error occurs,
    fucntion returns None.
    """
    
    #Set the Error Catch
    error = None
    
    try:

        #ApplyEdits URL for Survey Table
        url = f'{approved_url}/{layer}/applyEdits'

        #Create Upload Parameters
        params = {
            'f':'json',
            'token':token,
            'updates':f'{package}'
        }


        #Initiate Update to AGOL
        response = requests.post(url, params)

        #If Response Connected
        if response.status_code == 200:

            #Create JSON Dict from Response
            response = response.json()

            #If Response Update was NOT Successfull, Create Error Log
            if response['updateResults'][0]['success'] == False:

                error = {   'Event':'Uploading Weekly Update Package to Approved Project Information Feature Layer Failed',
                            'OBJID': response['updateResults'][0]['uniqueId'],
                            'Code': response['updateResults'][0]['error']['code'],
                            'Details': response['updateResults'][0]['error']['description']}
                
                raise Exception("Failed to Upload Approved Project Data to AGOL")


        #If there is a failure to connect
        elif response.status_code == 400:

            error = {   'Event': 'Failed to Connect',
                        'OBJID': '',
                        'Code': response['error']['code'],
                        'Details': response['error']['details'] }
            
            raise Exception("Failed to Connect to AGOL")


        #If Response Didn't Connect, Raise Exception
        else:

            error = {   'Event': 'Failed to Connect',
                        'OBJID': '',
                        'Code':'',
                        'Details': '' }
            
            raise Exception("Failed to Connect to AGOL")




    #If Exception Occurred, Return Error
    except Exception as e:
            
            return error