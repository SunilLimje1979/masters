from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from .models import *
# from .serializers import  *
from rest_framework import serializers
from django.db.models import Q
from django.utils import timezone
from rest_framework.decorators import api_view
from medicify_project.models import * 
from medicify_project.serializers import *
from django.contrib.auth import authenticate
from datetime import datetime
# Create your views here.

@api_view(['POST'])
def get_datacodemaster(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
        

    DataCodeId = request.data.get('DataCodeId', '')

    if not DataCodeId:
        res = {'message_code': 999, 'message_text': 'Data code id is required.'}
    else:
        try:
            
            # Fetch data using Django ORM
            datacodemaster = Tbldatacodemaster.objects.filter(
                Q(datacodeid=DataCodeId)
            )

            # Serialize the data
            serializer = DataCodeMasterSerializer(datacodemaster, many=True)
            result = serializer.data

            if result:
                res = {
                    'message_code': 1000,
                    'message_text': "Data code masters retrieved successfully.",
                    'message_data': result,
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }
            else:
                res = {
                    'message_code': 999,
                    'message_text': "Data code masters for this data code id not found.",
                    'message_data': [],
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f"Error: {str(e)}"}

    return Response(res, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def insert_datacodemaster(request):
    
#     debug = ""
#     res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
     
#     # Extract data from request
#     DataCodeName = request.data.get('DataCodeName', '')
#     DataCodeValue = request.data.get('DataCodeValue', '')
#     DataCodeDescription = request.data.get('DataCodeDescription', '')

#     # Validate appointment_id
#     if not DataCodeName:
#         res = {'message_code': 999,'message_text': 'Data code name is required'}
#     elif not DataCodeValue:
#         res = {'message_code': 999,'message_text': 'Data code value is required'}
#     elif not DataCodeDescription:
#         res = {'message_code': 999,'message_text': 'Data code description is required'}
#     else:
#         try:
            
#             datacodemaster = Tbldatacodemaster.objects.create(
#                 datacodename=DataCodeName,
#                 datacodevalue=DataCodeValue,
#                 datacodedescription=DataCodeDescription
#             )

#             res = {
#                 'message_code': 1000,
#                 'message_text': 'Data code master insert successfully',
#                 'message_data':{'DataCodeId': str(datacodemaster.datacodeid)},
#                 'message_debug': [{"Debug": debug}] if debug != "" else []
#             }

#         except Tbldatacodemaster.DoesNotExist:
#             res = {'message_code': 999, 'message_text': 'DataCodeMaster not found'}

#         except Exception as e:
#             res = {'message_code': 999, 'message_text': f'Error: {str(e)}'}

#     return Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def update_datacodemaster(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
     
    # Extract data from request
    DataCodeId = request.data.get('DataCodeId', '')
    DataCodeName = request.data.get('DataCodeName', '')
    DataCodeValue = request.data.get('DataCodeValue', '')
    DataCodeDescription = request.data.get('DataCodeDescription', '')

    # Validate DataCodeId
    if not DataCodeId:
        res = {'message_code': 999, 'message_text': 'Data code id is required'}
    elif not DataCodeName:
        res = {'message_code': 999,'message_text': 'Data code name is required'}
    elif not DataCodeValue:
        res = {'message_code': 999,'message_text': 'Data code value is required'}
    elif not DataCodeDescription:
        res = {'message_code': 999,'message_text': 'Data code description is required'}
    else:
        try:
            # Retrieve the DataCodeMaster instance using ORM
            datacodemaster = Tbldatacodemaster.objects.get(datacodeid=DataCodeId)

            # Update the DataCodeMaster fields
            datacodemaster.datacodename = DataCodeName
            datacodemaster.datacodevalue = DataCodeValue
            datacodemaster.datacodedescription = DataCodeDescription
            datacodemaster.save()

            res = {
                'message_code': 1000,
                'message_text': 'Data code master updated successfully',
                'message_data': {'DataCodeId': str(datacodemaster.datacodeid)},
                'message_debug': [{"Debug": debug}] if debug != "" else []
            }

        except Tbldatacodemaster.DoesNotExist:
            res = {'message_code': 999, 'message_text': 'DataCodeMaster not found'}

        except Exception as e:
            res = {'message_code': 999, 'message_text': f'Error: {str(e)}'}

    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def delete_datacodemaster(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
    
    DataCodeId = request.data.get('DataCodeId', '')

    if not DataCodeId:
        res = {'message_code': 999, 'message_text': 'Data code id is required.'}
    else:
        try:
            # Fetch data using Django ORM
            datacodemaster = Tbldatacodemaster.objects.filter(datacodeid=DataCodeId)

            # Check if the data exists
            if datacodemaster.exists():
                # Delete the data
                datacodemaster.delete()

                res = {
                    'message_code': 1000,
                    'message_text': "Data code master deleted successfully.",
                    'message_data': [{'DataCodeId': DataCodeId}],
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }
            else:
                res = {
                    'message_code': 999,
                    'message_text': "Data code master not found.",
                    'message_data': [],
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f"Error: {str(e)}"}

    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_medicine_instruction(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
        

    doctor_instruction_id = request.data.get('Doctor_Instruction_Id', '')

    if not doctor_instruction_id:
        res = {'message_code': 999, 'message_text': 'Doctor instruction id is required.'}
    else:
        try:
            
            # Fetch data using Django ORM
            medicine_instruction = TblmedicineInstructions.objects.filter(
                Q(doctor_instruction_id=doctor_instruction_id)
            )

            # Serialize the data
            serializer = TblmedicineInstructionsSerializer(medicine_instruction, many=True)
            result = serializer.data

            if result:
                res = {
                    'message_code': 1000,
                    'message_text': "Medicine instruction retrieved successfully.",
                    'message_data': result,
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }
            else:
                res = {
                    'message_code': 999,
                    'message_text': "Medicine instruction for this doctor instruction id not found.",
                    'message_data': [],
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f"Error: {str(e)}"}

    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def delete_medicine_instruction(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
    
    doctor_instruction_id = request.data.get('Doctor_Instruction_Id', '')

    if not doctor_instruction_id:
        res = {'message_code': 999, 'message_text': 'Doctor instruction id is required.'}
    else:
        try:
            # Fetch data using Django ORM
            medicine_instruction = TblmedicineInstructions.objects.filter(doctor_instruction_id=doctor_instruction_id)

            # Check if the data exists
            if medicine_instruction.exists():
                # Delete the data
                medicine_instruction.delete()

                res = {
                    'message_code': 1000,
                    'message_text': "Medicine instructions deleted successfully",
                    'message_data': [{'Doctor_Instruction_Id': doctor_instruction_id}],
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }
            else:
                res = {
                    'message_code': 999,
                    'message_text': "Medicine instructions not found.",
                    'message_data': [],
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f"Error: {str(e)}"}

    return Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def insert_medicine_instruction(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
    
    # Extract data from request
    doctor_id = request.data.get('Doctor_Id', '')
    instruction_language = request.data.get('Instruction_Language', '')
    instruction_text = request.data.get('Instruction_Text', '')

    # Validate inputs
    if not doctor_id:
        res = {'message_code': 999, 'message_text': 'Doctor id is required.'}
    elif not instruction_language:
        res = {'message_code': 999, 'message_text': 'Instruction language is required.'}
    elif not instruction_text:
        res = {'message_code': 999, 'message_text': 'Instruction text is required.'}
    else:
        try:
                
                medicine_data = {'doctor_id':doctor_id,
                        'instruction_language':instruction_language,
                         'instruction_text':instruction_text
                }
                medicine_instructionSerializer = TblmedicineInstructionsSerializer(data=medicine_data)
                if medicine_instructionSerializer.is_valid():
                    instance = medicine_instructionSerializer.save()
                    last_doctor_medicine_id = instance.doctor_instruction_id

                    res = {
                        'message_code': 1000,
                        'message_text': 'Success',
                        'message_data': {'last_doctor_medicine_id': str(last_doctor_medicine_id)},
                        'message_debug': debug if debug else []
                    }
                else:
                    res = {
                        'message_code': 2000,
                        'message_text': 'Validation Error',
                        'message_errors': medicine_instructionSerializer.errors
                    }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f'Unable to insert Medicine instructions. Error: {str(e)}',
                   'message_data': [],
                   'message_debug': [] if debug == "" else [{'Debug': debug}]}

    return Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def update_medicine_instruction(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}

    # Extract data from request
    doctor_instruction_id = request.data.get('Doctor_Instruction_Id', '')
    doctor_id = request.data.get('Doctor_Id', '')
    instruction_language = request.data.get('Instruction_Language', '')
    instruction_text = request.data.get('Instruction_Text', '')

    # Validate inputs
    if not doctor_instruction_id:
        res = {'message_code': 999, 'message_text': 'Doctor instruction id is required.'}
    elif not doctor_id:
        res = {'message_code': 999, 'message_text': 'Doctor id is required.'}
    elif not instruction_language:
        res = {'message_code': 999, 'message_text': 'Instruction language is required.'}
    elif not instruction_text:
        res = {'message_code': 999, 'message_text': 'Instruction text is required.'}
    else:
        try:
            # Get MedicineInstructions instance
            medicine_data = {'doctor_id':doctor_id,
                        'instruction_language':instruction_language,
                         'instruction_text':instruction_text
                }
            medicine_instruction = TblmedicineInstructions.objects.get(doctor_instruction_id=doctor_instruction_id)


            serializer = TblmedicineInstructionsSerializer(medicine_instruction, data=medicine_data, partial=True)
            if serializer.is_valid():
                updated_data = serializer.validated_data  # Get the validated data after a successful update
                serializer.save()

                res = {
                        'message_code': 1000,
                        'message_text': 'Success',
                        'message_data': {'Doctor_Instruction_Id': str(doctor_instruction_id)},
                        'message_debug': debug if debug else []
                    }
            else:
                    res = {
                        'message_code': 2000,
                        'message_text': 'Validation Error',
                        'message_errors': serializer.errors
                    }

            
        except TblmedicineInstructions.DoesNotExist:
            res = {'message_code': 999, 'message_text': 'MedicineInstructions not found'}

        except Exception as e:
            res = {'message_code': 999, 'message_text': f'Error: {str(e)}',
                   'message_data': [],
                   'message_debug': [] if debug == "" else [{'Debug': debug}]}

    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_datacodemaster_byname(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
        

    DataCodeName = request.data.get('DataCodeName', '')

    if not DataCodeName:
        res = {'message_code': 999, 'message_text': 'Data code name is required.'}
    else:
        try:
            
            # Fetch data using Django ORM
            datacodemaster = Tbldatacodemaster.objects.filter(
                Q(datacodename__iexact=DataCodeName)
            )

            # Serialize the data
            serializer = DataCodeMasterSerializer(datacodemaster, many=True)
            result = serializer.data

            if result:
                res = {
                    'message_code': 1000,
                    'message_text': "Data code masters retrieved successfully.",
                    'message_data': result,
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }
            else:
                res = {
                    'message_code': 999,
                    'message_text': "Data code masters for this data code name not found.",
                    'message_data': [],
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f"Error: {str(e)}"}

    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_medicine_instructionsbydoctorId(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
        

    doctor_id = request.data.get('Doctor_Id', '')

    if not doctor_id:
        res = {'message_code': 999, 'message_text': 'Doctor id is required.'}
    else:
        try:
            
            # Fetch data using Django ORM
            medicine_instructionbydoctor_id = TblmedicineInstructions.objects.filter(
                Q(doctor_id=doctor_id)
            )

            # Serialize the data
            serializer = TblmedicineInstructionsSerializer(medicine_instructionbydoctor_id, many=True)
            result = serializer.data

            if result:
                res = {
                    'message_code': 1000,
                    'message_text': "Medicine instruction by doctor id retrieved successfully.",
                    'message_data': result,
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }
            else:
                res = {
                    'message_code': 999,
                    'message_text': "Medicine instruction for this doctor instruction id not found.",
                    'message_data': [],
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f"Error: {str(e)}"}

    return Response(res, status=status.HTTP_200_OK)


###########################new updated api of datacodemaster
@api_view(["POST"])
def insert_datacodemaster(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Functional part is commented.',
        'message_data': [],
        'message_debug': debug
    }

    serializer = DataCodeMasterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        response_data['message_code'] = 1000
        response_data['message_text'] = 'Data code master inserted successfully'
        response_data['message_data'] = {'datacodemaster_details': serializer.data}
    else:
        response_data['message_text'] = 'Invalid data provided.'
        response_data['message_data'] = serializer.errors

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["POST"])
def get_datacodemaster_by_name_and_doctor(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Functional part is commented.',
        'message_data': [],
        'message_debug': debug
    }

    datacodename = request.data.get('datacodename', None)
    doctor_id = request.data.get('doctor_id', None)

    if not datacodename:
        response_data['message_text'] = 'Data code name is required.'
        return Response(response_data, status=status.HTTP_200_OK)
    
    if doctor_id is not None:
        datacodes = Tbldatacodemaster.objects.filter(datacodename=datacodename, doctor_id=doctor_id)
    else:
        datacodes = Tbldatacodemaster.objects.filter(datacodename=datacodename, doctor_id__isnull=True)

    if not datacodes.exists():
        response_data['message_text'] = 'No data code masters found.'
        return Response(response_data, status=status.HTTP_200_OK)

    # Serialize the data
    serializer = DataCodeMasterSerializer(datacodes, many=True)

    response_data['message_code'] = 1000
    response_data['message_text'] = 'Data code masters retrieved successfully.'
    response_data['message_data'] = serializer.data

    return Response(response_data, status=status.HTTP_200_OK)


# @api_view(["POST"])
# def update_datacodemaster_byid(request):
#     debug = []
#     response_data = {
#         'message_code': 999,
#         'message_text': 'Functional part is commented.',
#         'message_data': [],
#         'message_debug': debug
#     }

#     datacodeid = request.data.get('datacodeid', None)
#     if not datacodeid:
#         response_data['message_text'] = 'Data code ID is required.'
#         return Response(response_data, status=status.HTTP_200_OK)

#     try:
#         datacodemaster = Tbldatacodemaster.objects.get(pk=datacodeid)
#     except Tbldatacodemaster.DoesNotExist:
#         response_data['message_text'] = 'Data code master not found.'
#         return Response(response_data, status=status.HTTP_200_OK)

#     serializer = DataCodeMasterSerializer(datacodemaster, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         response_data['message_code'] = 1000
#         response_data['message_text'] = 'Data code master updated successfully.'
#         response_data['message_data'] = serializer.data
#         return Response(response_data, status=status.HTTP_200_OK)
#     else:
#         response_data['message_text'] = 'Invalid data.'
#         response_data['message_debug'] = serializer.errors
#         return Response(response_data, status=status.HTTP_200_OK)

@api_view(["POST"])
def update_datacodemaster_byid(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Functional part is commented.',
        'message_data': [],
        'message_debug': debug
    }

    datacodeid = request.data.get('datacodeid', None)
    datacodename = request.data.get('datacodename', None)

    if not datacodeid:
        response_data['message_text'] = 'Data code ID is required.'
        return Response(response_data, status=status.HTTP_200_OK)

    if not datacodename:
        response_data['message_text'] = 'Data code name is required.'
        return Response(response_data, status=status.HTTP_200_OK)

    try:
        datacodemaster = Tbldatacodemaster.objects.get(datacodeid=datacodeid, datacodename=datacodename)
    except Tbldatacodemaster.DoesNotExist:
        response_data['message_text'] = 'Data code master not found.'
        return Response(response_data, status=status.HTTP_200_OK)

    serializer = DataCodeMasterSerializer(datacodemaster, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        response_data['message_code'] = 1000
        response_data['message_text'] = 'Data code master updated successfully.'
        response_data['message_data'] = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        response_data['message_text'] = 'Invalid data.'
        response_data['message_debug'] = serializer.errors
        return Response(response_data, status=status.HTTP_200_OK)
    
@api_view(["POST"])
def login(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    username = request.data.get('username', None)
    password = request.data.get('password', None)

    if not username:
        response_data['message_text'] = 'Username is required.'
    elif not password:
        response_data['message_text'] = 'Password is required.'
    else:
        user = authenticate(username=username, password=password)
        if user:
            response_data['message_code'] = 1000
            response_data['message_text'] = 'Login successful.'
            response_data['message_data'] = {'username': username,'user_id':user.id}
        else:
            response_data['message_text'] = 'Invalid credentials'

    return Response(response_data, status=status.HTTP_200_OK)
# from django.forms.models import model_to_dict
# @api_view(["POST"])
# def login(request):
#     debug = []
#     response_data = {
#         'message_code': 999,
#         'message_text': 'Error occurred.',
#         'message_data': [],
#         'message_debug': debug
#     }

#     username = request.data.get('username', None)
#     password = request.data.get('password', None)

#     if not username:
#         response_data['message_text'] = 'Username is required.'
#     elif not password:
#         response_data['message_text'] = 'Password is required.'
#     else:
#         user = authenticate(username=username, password=password)
#         if user:
#             response_data['message_code'] = 1000
#             response_data['message_text'] = 'Login successful.'
#             user_data = model_to_dict(user)  # Convert user instance to dictionary
#             response_data['message_data'] = user_data
#         else:
#             response_data['message_text'] = 'Invalid credentials'

#     return Response(response_data, status=status.HTTP_200_OK)


###########################TableLead API's ##################
@api_view(["POST"])
def insert_lead(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    try:
        data = request.data.copy()
        current_month_year = datetime.now().strftime("%Y-%m")
        data['lead_month_year'] = current_month_year

        # Convert current date and time to epoch for lead_date_time_stamp
        current_epoch_time = int(datetime.now().timestamp())
        data['lead_date_time_stamp'] = current_epoch_time

        # Convert lead_dob to epoch if provided
        lead_dob = data.get('lead_dob')
        if lead_dob:
            try:
                dt = datetime.strptime(lead_dob, "%Y-%m-%d")
                epoch = int(dt.timestamp())
                data['lead_dob'] = epoch
            except ValueError as e:
                response_data['message_text'] = 'Invalid date format for lead_dob. It should be YYYY-MM-DD.'
                response_data['message_debug'].append(str(e))
                return Response(response_data, status=status.HTTP_200_OK)

        serializer = TblLeadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data['message_code'] = 1000
            response_data['message_text'] = 'Lead inserted successfully.'
            response_data['message_data'] = serializer.data
        else:
            response_data['message_text'] = 'Invalid data.'
            response_data['message_debug'] = serializer.errors

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["POST"])
def get_all_leads(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    try:
        leads = TblLead.objects.all()
        serializer = TblLeadSerializer(leads, many=True)
        lead_data = serializer.data

        # Convert lead_dob from epoch to normal date format
        for lead in lead_data:
            lead_dob = lead.get('lead_dob')
            if lead_dob:
                try:
                    normal_date = datetime.fromtimestamp(lead_dob).strftime("%Y-%m-%d")
                    lead['lead_dob'] = normal_date
                except Exception as e:
                    debug.append(f"Error converting epoch to date for lead_id {lead['lead_id']}: {str(e)}")

        response_data['message_code'] = 1000
        response_data['message_text'] = 'Leads retrieved successfully.'
        response_data['message_data'] = lead_data

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(["POST"])
def get_lead_by_id(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    try:
        lead_id = request.data.get('lead_id')
        if not lead_id:
            response_data['message_text'] = 'Lead ID is required.'
            return Response(response_data, status=status.HTTP_200_OK)

        try:
            lead = TblLead.objects.get(pk=lead_id)
        except TblLead.DoesNotExist:
            response_data['message_text'] = 'Lead not found.'
            return Response(response_data, status=status.HTTP_200_OK)

        serializer = TblLeadSerializer(lead)
        lead_data = serializer.data

        # Convert lead_dob from epoch to normal date format
        lead_dob = lead_data.get('lead_dob')
        if lead_dob:
            try:
                normal_date = datetime.fromtimestamp(lead_dob).strftime("%Y-%m-%d")
                lead_data['lead_dob'] = normal_date
            except Exception as e:
                debug.append(f"Error converting epoch to date for lead_id {lead_id}: {str(e)}")

        response_data['message_code'] = 1000
        response_data['message_text'] = 'Lead retrieved successfully.'
        response_data['message_data'] = lead_data

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["POST"])
def update_lead(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    try:
        lead_id = request.data.get('lead_id')
        if not lead_id:
            response_data['message_text'] = 'Lead ID is required.'
            return Response(response_data, status=status.HTTP_200_OK)

        try:
            lead = TblLead.objects.get(pk=lead_id)
        except TblLead.DoesNotExist:
            response_data['message_text'] = 'Lead not found.'
            return Response(response_data, status=status.HTTP_200_OK)

        data = request.data.copy()

        # Convert lead_dob to epoch if provided
        lead_dob = data.get('lead_dob')
        if lead_dob:
            try:
                dt = datetime.strptime(lead_dob, "%Y-%m-%d")
                epoch = int(dt.timestamp())
                data['lead_dob'] = epoch
            except ValueError as e:
                response_data['message_text'] = 'Invalid date format for lead_dob. It should be YYYY-MM-DD.'
                response_data['message_debug'].append(str(e))
                return Response(response_data, status=status.HTTP_200_OK)

        serializer = TblLeadSerializer(lead, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data['message_code'] = 1000
            response_data['message_text'] = 'Lead updated successfully.'
            response_data['message_data'] = serializer.data
        else:
            response_data['message_text'] = 'Invalid data.'
            response_data['message_debug'] = serializer.errors

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["POST"])
def get_leads_by_handler_or_by_id(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    try:
        lead_by_id = request.data.get('lead_by_id')
        lead_handler_id = request.data.get('lead_handler_id')

        if not lead_by_id and not lead_handler_id:
            response_data['message_text'] = 'Lead by ID or Lead Handler ID is required.'
            return Response(response_data, status=status.HTTP_200_OK)

        if lead_by_id:
            leads = TblLead.objects.filter(lead_by_id=lead_by_id)
        elif lead_handler_id:
            leads = TblLead.objects.filter(lead_handler_id=lead_handler_id)
        else:
            leads = TblLead.objects.none()

        if not leads.exists():
            response_data['message_text'] = 'No data found for given ID.'
            return Response(response_data, status=status.HTTP_200_OK)

        leads_data = []
        for lead in leads:
            lead_data = TblLeadSerializer(lead).data

            # Convert lead_dob from epoch to date format
            lead_dob = lead_data.get('lead_dob')
            if lead_dob:
                try:
                    dt = datetime.fromtimestamp(int(lead_dob))
                    lead_data['lead_dob'] = dt.strftime("%Y-%m-%d")
                except ValueError as e:
                    response_data['message_debug'].append(f"Invalid epoch value for lead_dob: {lead_dob}")

            leads_data.append(lead_data)

        response_data['message_code'] = 1000
        response_data['message_text'] = 'Leads retrieved successfully.'
        response_data['message_data'] = leads_data

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)


###########################TblLeadFollowUp API's ##########################
@api_view(["POST"])
def insert_lead_followup(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    try:
        data = request.data.copy()

        # Check if lead_id, follow_up_by, and follow_up_user_id are provided
        lead_id = data.get('lead_id')
        follow_up_by = data.get('follow_up_by')
        follow_up_user_id = data.get('follow_up_user_id')

        if not lead_id:
            response_data['message_text'] = 'Lead ID is required.'
            return Response(response_data, status=status.HTTP_200_OK)

        if not follow_up_by:
            response_data['message_text'] = 'Follow Up By is required.'
            return Response(response_data, status=status.HTTP_200_OK)

        if not follow_up_user_id:
            response_data['message_text'] = 'Follow Up User ID is required.'
            return Response(response_data, status=status.HTTP_200_OK)

        # Function to convert datetime to epoch
        def convert_to_epoch(date_time_str):
            formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]
            for fmt in formats:
                try:
                    dt = datetime.strptime(date_time_str, fmt)
                    return int(dt.timestamp())
                except ValueError:
                    continue
            raise ValueError(f"Invalid date format: {date_time_str}. Expected formats: {formats}")

        # Convert follow_up_date_time_stamp to epoch if provided
        follow_up_date_time_stamp = data.get('follow_up_date_time_stamp')
        if follow_up_date_time_stamp:
            try:
                data['follow_up_date_time_stamp'] = convert_to_epoch(follow_up_date_time_stamp)
            except ValueError as e:
                response_data['message_text'] = str(e)
                response_data['message_debug'].append(str(e))
                return Response(response_data, status=status.HTTP_200_OK)

        # Convert next_follow_up_date_time_stamp to epoch if provided
        next_follow_up_date_time_stamp = data.get('next_follow_up_date_time_stamp')
        if next_follow_up_date_time_stamp:
            try:
                data['next_follow_up_date_time_stamp'] = convert_to_epoch(next_follow_up_date_time_stamp)
            except ValueError as e:
                response_data['message_text'] = str(e)
                response_data['message_debug'].append(str(e))
                return Response(response_data, status=status.HTTP_200_OK)

        # Assign current date and time to created_on and convert to epoch
        current_datetime = datetime.now()
        data['created_on'] = int(current_datetime.timestamp())

        serializer = TblLeadFollowUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data['message_code'] = 1000
            response_data['message_text'] = 'Lead follow-up inserted successfully.'
            response_data['message_data'] = serializer.data
        else:
            response_data['message_text'] = 'Invalid data.'
            response_data['message_debug'] = serializer.errors

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)


# @api_view(["POST"])
# def get_followups_by_lead_id(request):
#     debug = []
#     response_data = {
#         'message_code': 999,
#         'message_text': 'Error occurred.',
#         'message_data': [],
#         'message_debug': debug
#     }

#     lead_id = request.data.get('lead_id', None)

#     if not lead_id:
#         response_data['message_text'] = 'Lead ID is required.'
#         return Response(response_data, status=status.HTTP_200_OK)

#     try:
#         follow_ups = TblLeadFollowUp.objects.filter(lead_id=lead_id).order_by('-created_on')
        
#         if not follow_ups.exists():
#             response_data['message_text'] = 'No data found for given lead ID.'
#         else:
#             follow_up_list = []
#             for follow_up in follow_ups:
#                 follow_up_data = TblLeadFollowUpSerializer(follow_up).data
#                 follow_up_data['follow_up_date_time_stamp'] = datetime.fromtimestamp(follow_up_data['follow_up_date_time_stamp']).strftime('%d-%m-%Y %H:%M:%S') if follow_up_data['follow_up_date_time_stamp'] else None
#                 follow_up_data['next_follow_up_date_time_stamp'] = datetime.fromtimestamp(follow_up_data['next_follow_up_date_time_stamp']).strftime('%d-%m-%Y %H:%M:%S') if follow_up_data['next_follow_up_date_time_stamp'] else None
#                 follow_up_list.append(follow_up_data)

#             response_data['message_code'] = 1000
#             response_data['message_text'] = 'Success'
#             response_data['message_data'] = follow_up_list

#     except Exception as e:
#         response_data['message_text'] = str(e)
#         debug.append(str(e))

#     return Response(response_data, status=status.HTTP_200_OK)

@api_view(["POST"])
def get_followups_by_lead_id(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    lead_id = request.data.get('lead_id', None)

    if not lead_id:
        response_data['message_text'] = 'Lead ID is required.'
        return Response(response_data, status=status.HTTP_200_OK)

    try:
        follow_ups = TblLeadFollowUp.objects.filter(lead_id=lead_id).order_by('-created_on')
        
        if not follow_ups.exists():
            response_data['message_text'] = 'No data found for given lead ID.'
        else:
            follow_up_list = []
            for follow_up in follow_ups:
                follow_up_data = TblLeadFollowUpSerializer(follow_up).data
                follow_up_data['follow_up_date_time_stamp'] = datetime.fromtimestamp(follow_up_data['follow_up_date_time_stamp']).strftime('%d-%m-%Y %I:%M:%S %p') if follow_up_data['follow_up_date_time_stamp'] else None
                follow_up_data['next_follow_up_date_time_stamp'] = datetime.fromtimestamp(follow_up_data['next_follow_up_date_time_stamp']).strftime('%d-%m-%Y %I:%M:%S %p') if follow_up_data['next_follow_up_date_time_stamp'] else None
                follow_up_list.append(follow_up_data)

            response_data['message_code'] = 1000
            response_data['message_text'] = 'Success'
            response_data['message_data'] = follow_up_list

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)


########################### Get API's for Countries,States and Cities
@api_view(['POST'])
def get_all_countries(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    try:
        countries = TblCountries.objects.all()
        if not countries.exists():
            response_data['message_text'] = 'No countries found.'
        else:
            serializer = TblCountriesSerializer(countries, many=True)
            response_data['message_code'] = 1000
            response_data['message_text'] = 'Success'
            response_data['message_data'] = serializer.data
    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_country_by_id(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    country_id = request.data.get('id', None)

    if not country_id:
        response_data['message_text'] = 'Country ID is required.'
        return Response(response_data, status=status.HTTP_200_OK)

    try:
        country = TblCountries.objects.get(id=country_id)
        serializer = TblCountriesSerializer(country)
        response_data['message_code'] = 1000
        response_data['message_text'] = 'Success'
        response_data['message_data'] = serializer.data
    except TblCountries.DoesNotExist:
        response_data['message_text'] = 'No country found for the given ID.'
    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_all_states(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': [],
        'message_debug': debug
    }

    try:
        states = TblStates.objects.all()
        serializer = TblStatesSerializer(states, many=True)
        response_data['message_code'] = 1000
        response_data['message_text'] = 'Success'
        response_data['message_data'] = serializer.data
    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)

#Using Nested Serailizer
# @api_view(['POST'])
# def get_states_by_country_id(request):
#     debug = []
#     response_data = {
#         'message_code': 999,
#         'message_text': 'Error occurred.',
#         'message_data': [],
#         'message_debug': debug
#     }

#     country_id = request.data.get('country_id', None)

#     if not country_id:
#         response_data['message_text'] = 'Country ID is required.'
#         return Response(response_data, status=status.HTTP_200_OK)

#     try:
#         states = TblStates.objects.filter(country=country_id)
        
#         if not states.exists():
#             response_data['message_text'] = 'No data found for the given country ID.'
#         else:
#             serializer = NestedTblStatesSerializer(states, many=True)
#             response_data['message_code'] = 1000
#             response_data['message_text'] = 'Success'
#             response_data['message_data'] = serializer.data

#     except Exception as e:
#         response_data['message_text'] = str(e)
#         debug.append(str(e))

#     return Response(response_data, status=status.HTTP_200_OK)

#Using Simple Serializers
@api_view(['POST'])
def get_states_by_country_id(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': {},
        'message_debug': debug
    }

    country_id = request.data.get('country_id', None)

    if not country_id:
        response_data['message_text'] = 'Country ID is required.'
        return Response(response_data, status=status.HTTP_200_OK)

    try:
        country = TblCountries.objects.filter(id=country_id).first()
        if not country:
            response_data['message_text'] = 'No country found for the given ID.'
            return Response(response_data, status=status.HTTP_200_OK)
        
        states = TblStates.objects.filter(country=country_id)
        
        if not states.exists():
            response_data['message_text'] = 'No states found for the given country ID.'
        else:
            country_serializer = TblCountriesSerializer(country)
            states_serializer = TblStatesSerializer(states, many=True)
            
            response_data['message_code'] = 1000
            response_data['message_text'] = 'Success'
            response_data['message_data'] = {
                'country': country_serializer.data,
                'states': states_serializer.data
            }

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_state_by_id(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': {},
        'message_debug': debug
    }

    state_id = request.data.get('state_id', None)

    if not state_id:
        response_data['message_text'] = 'State ID is required.'
        return Response(response_data, status=status.HTTP_200_OK)

    try:
        state = TblStates.objects.filter(id=state_id).first()
        if not state:
            response_data['message_text'] = 'No state found for the given ID.'
            return Response(response_data, status=status.HTTP_200_OK)
        
        country = TblCountries.objects.filter(id=state.country_id).first()
        
        if not country:
            response_data['message_text'] = 'No country found for the given state\'s country ID.'
            return Response(response_data, status=status.HTTP_200_OK)
        
        country_serializer = TblCountriesSerializer(country)
        state_serializer = TblStatesSerializer(state)
        
        response_data['message_code'] = 1000
        response_data['message_text'] = 'Success'
        response_data['message_data'] = {
            'country': country_serializer.data,
            'state': state_serializer.data
        }

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_cities_by_state_id(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': {},
        'message_debug': debug
    }

    state_id = request.data.get('state_id', None)

    if not state_id:
        response_data['message_text'] = 'State ID is required.'
        return Response(response_data, status=status.HTTP_200_OK)

    try:
        state = TblStates.objects.filter(id=state_id).first()
        if not state:
            response_data['message_text'] = 'No state found for the given ID.'
            return Response(response_data, status=status.HTTP_200_OK)
        
        country = TblCountries.objects.filter(id=state.country_id).first()
        cities = TblCities.objects.filter(state=state_id)
        
        if not cities.exists():
            response_data['message_text'] = 'No cities found for the given state ID.'
        else:
            country_serializer = TblCountriesSerializer(country)
            state_serializer = TblStatesSerializer(state)
            cities_serializer = TblCitiesSerializer(cities, many=True)
            
            response_data['message_code'] = 1000
            response_data['message_text'] = 'Success'
            response_data['message_data'] = {
                'country': country_serializer.data,
                'state': state_serializer.data,
                'cities': cities_serializer.data
            }

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_city_by_id(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': {},
        'message_debug': debug
    }

    city_id = request.data.get('city_id', None)

    if not city_id:
        response_data['message_text'] = 'City ID is required.'
        return Response(response_data, status=status.HTTP_200_OK)

    try:
        city = TblCities.objects.filter(id=city_id).first()
        if not city:
            response_data['message_text'] = 'No city found for the given ID.'
            return Response(response_data, status=status.HTTP_200_OK)
        
        state = TblStates.objects.filter(id=city.state_id).first()
        if not state:
            response_data['message_text'] = 'No state found for the given city\'s state ID.'
            return Response(response_data, status=status.HTTP_200_OK)
        
        country = TblCountries.objects.filter(id=state.country_id).first()
        if not country:
            response_data['message_text'] = 'No country found for the given state\'s country ID.'
            return Response(response_data, status=status.HTTP_200_OK)

        country_serializer = TblCountriesSerializer(country)
        state_serializer = TblStatesSerializer(state)
        city_serializer = TblCitiesSerializer(city)
        
        response_data['message_code'] = 1000
        response_data['message_text'] = 'Success'
        response_data['message_data'] = {
            'country': country_serializer.data,
            'state': state_serializer.data,
            'city': city_serializer.data
        }

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_cities_by_state_and_country(request):
    debug = []
    response_data = {
        'message_code': 999,
        'message_text': 'Error occurred.',
        'message_data': {},
        'message_debug': debug
    }

    state_id = request.data.get('state_id', None)
    country_id = request.data.get('country_id', None)

    if not state_id:
        response_data['message_text'] = 'State ID is required.'
        return Response(response_data, status=status.HTTP_200_OK)

    if not country_id:
        response_data['message_text'] = 'Country ID is required.'
        return Response(response_data, status=status.HTTP_200_OK)

    try:
        state = TblStates.objects.filter(id=state_id, country_id=country_id).first()
        if not state:
            response_data['message_text'] = 'No state found for the given state ID and country ID.'
            return Response(response_data, status=status.HTTP_200_OK)

        country = TblCountries.objects.filter(id=country_id).first()
        if not country:
            response_data['message_text'] = 'No country found for the given country ID.'
            return Response(response_data, status=status.HTTP_200_OK)

        cities = TblCities.objects.filter(state_id=state_id)
        if not cities.exists():
            response_data['message_text'] = 'No cities found for the given state ID.'
            return Response(response_data, status=status.HTTP_200_OK)

        country_serializer = TblCountriesSerializer(country)
        state_serializer = TblStatesSerializer(state)
        cities_serializer = TblCitiesSerializer(cities, many=True)

        response_data['message_code'] = 1000
        response_data['message_text'] = 'Success'
        response_data['message_data'] = {
            'country': country_serializer.data,
            'state': state_serializer.data,
            'cities': cities_serializer.data
        }

    except Exception as e:
        response_data['message_text'] = str(e)
        debug.append(str(e))

    return Response(response_data, status=status.HTTP_200_OK)

