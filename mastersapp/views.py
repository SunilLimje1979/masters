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


@api_view(['POST'])
def insert_datacodemaster(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
     
    # Extract data from request
    DataCodeName = request.data.get('DataCodeName', '')
    DataCodeValue = request.data.get('DataCodeValue', '')
    DataCodeDescription = request.data.get('DataCodeDescription', '')

    # Validate appointment_id
    if not DataCodeName:
        res = {'message_code': 999,'message_text': 'Data code name is required'}
    elif not DataCodeValue:
        res = {'message_code': 999,'message_text': 'Data code value is required'}
    elif not DataCodeDescription:
        res = {'message_code': 999,'message_text': 'Data code description is required'}
    else:
        try:
            
            datacodemaster = Tbldatacodemaster.objects.create(
                datacodename=DataCodeName,
                datacodevalue=DataCodeValue,
                datacodedescription=DataCodeDescription
            )

            res = {
                'message_code': 1000,
                'message_text': 'Data code master insert successfully',
                'message_data':{'DataCodeId': str(datacodemaster.DataCodeId)},
                'message_debug': [{"Debug": debug}] if debug != "" else []
            }

        except Tbldatacodemaster.DoesNotExist:
            res = {'message_code': 999, 'message_text': 'DataCodeMaster not found'}

        except Exception as e:
            res = {'message_code': 999, 'message_text': f'Error: {str(e)}'}

    return Response(res, status=status.HTTP_200_OK)

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
                'message_data': {'DataCodeId': str(datacodemaster.DataCodeId)},
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
            # Create MedicineInstructions instance
            medicine_instruction = TblmedicineInstructions.objects.create(
                doctor_id=doctor_id,
                instruction_language=instruction_language,
                instruction_text=instruction_text
            )

            res = {
                'message_code': 1000,
                'message_text': 'Medicine instructions insert successfully.',
                'message_data': [{'Doctor_Instruction_Id': medicine_instruction.doctor_instruction_id}],
                'message_debug': [] if debug == "" else [{'Debug': debug}]
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
            medicine_instruction = TblmedicineInstructions.objects.get(doctor_instruction_id=doctor_instruction_id)

            # Update the fields
            medicine_instruction.doctor_id = doctor_id
            medicine_instruction.instruction_language = instruction_language
            medicine_instruction.instruction_text = instruction_text
            medicine_instruction.save()

            res = {
                'message_code': 1000,
                'message_text': 'Medicine instructions update successfully.',
                'message_data': [{'Doctor_Instruction_Id': medicine_instruction.doctor_instruction_id}],
                'message_debug': [] if debug == "" else [{'Debug': debug}]
            }

        except TblmedicineInstructions.DoesNotExist:
            res = {'message_code': 999, 'message_text': 'MedicineInstructions not found'}

        except Exception as e:
            res = {'message_code': 999, 'message_text': f'Error: {str(e)}',
                   'message_data': [],
                   'message_debug': [] if debug == "" else [{'Debug': debug}]}

    return Response(res, status=status.HTTP_200_OK)
