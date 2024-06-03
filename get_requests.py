import grequests
import ast
from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import APIRouter,Request,Form,Depends,HTTPException
from fastapi.responses import RedirectResponse
from http_basic import HTTPBasicCredentials,HTTPBasic
from starlette_context import context,middleware,plugins

from pathlib import Path



from typing import Annotated
router = APIRouter()
templates = Jinja2Templates(directory=f'{Path(__file__).parent}' + '/templates')
security = HTTPBasic()
def get_namescame():
    url = 'https://16.16.198.178.nip.io/0986525956Ee/id_name_secname'
    req = [grequests.get(url)]
    req = grequests.map(req)
    for i in req:


        return ast.literal_eval(i.text)

def get_all_subjects():
    url = ['https://16.16.198.178.nip.io/0986525956Ee/all_subjects']
    req = [grequests.get(url) for url in url]
    req = grequests.map(req)
    for i in req:

        return ast.literal_eval(i.text)

def get_dates_represent():
    url = ['https://16.16.198.178.nip.io/get_dates_represent']
    req = [grequests.get(url) for url in url]
    req = grequests.map(req)
    for i in req:

        return ast.literal_eval(i.text)

def get_schedule(day_index:int):
    url = [f'https://16.16.198.178.nip.io/get_schedule?day_index={day_index}']
    req = [grequests.get(url) for url in url]
    req = grequests.map(req)
    for i in req:

        return ast.literal_eval(i.text)
    



@router.get('/')
async def lobby(request:Request):
    
    return templates.TemplateResponse('main.html',{'request':request})





@router.get('/add_marks')
async def add_marks_url(request:Request):
    students = get_namescame()
    students_list  =[]
    for i in students:
        students_list.append([i[0],i[1] +' ' + i[2]])
    marks_list = [i for i in range(1,13)]

    return templates.TemplateResponse('add_mark.html',{'request':request,'marks_list' : marks_list,'student_list' : students_list,'subj_list': get_all_subjects(),'name':'idk'})


@router.get('/add_hw')
async def add_hw_url(request:Request):
    dates_represent = get_dates_represent()
    
    return templates.TemplateResponse('add_homework.html',{'request': request,'date_list':dates_represent,'name':'homework'})
    

@router.get('/schedule')
async def schedule_lobby(request:Request):

    return templates.TemplateResponse('schedule_main.html',{'request':request})


@router.get('/schedule/monday')
async def change_schedule_monday_url(request:Request,credentials: Annotated[HTTPBasicCredentials,Depends(security)]):
    schedule = get_schedule(0)
    title = 'Розклад на понеділок'
    route = 'https://16.16.198.178.nip.io/change_schedule?day_index=1'
    all_subjects = get_all_subjects()

    return templates.TemplateResponse('schedule.html',{'request':request,'title':title,'schedule':schedule,'all_subjects':all_subjects,'name':'schedule','route':route})


@router.get('/schedule/tuesday')
async def change_schedule_monday_url(request:Request,credentials: Annotated[HTTPBasicCredentials,Depends(security)]):
    schedule = get_schedule(1)
    title = 'Розклад на вівторок'
    route = 'https://16.16.198.178.nip.io/change_schedule?day_index=2'
    all_subjects = get_all_subjects()

    return templates.TemplateResponse('schedule.html',{'request':request,'title':title,'schedule':schedule,'all_subjects':all_subjects,'name':'schedule','route':route})

@router.get('/schedule/wednesday')
async def change_schedule_monday_url(request:Request,credentials: Annotated[HTTPBasicCredentials,Depends(security)]):
    schedule = get_schedule(2)
    title = 'Розклад на середу'
    route = 'https://16.16.198.178.nip.io/change_schedule?day_index=3'
    all_subjects = get_all_subjects()

    return templates.TemplateResponse('schedule.html',{'request':request,'title':title,'schedule':schedule,'all_subjects':all_subjects,'name':'schedule','route':route})


@router.get('/schedule/thursday')
async def change_schedule_monday_url(request:Request,credentials: Annotated[HTTPBasicCredentials,Depends(security)]):
    schedule = get_schedule(3)
    title = 'Розклад на четвер'
    route = 'https://16.16.198.178.nip.io/change_schedule?day_index=4'
    all_subjects = get_all_subjects()

    return templates.TemplateResponse('schedule.html',{'request':request,'title':title,'schedule':schedule,'all_subjects':all_subjects,'name':'schedule','route':route})


@router.get('/schedule/friday')
async def change_schedule_monday_url(request:Request,credentials: Annotated[HTTPBasicCredentials,Depends(security)]):
    schedule = get_schedule(4)
    title = "Розклад на п'ятницю"
    route = 'https://16.16.198.178.nip.io/change_schedule?day_index=5'
    all_subjects = get_all_subjects()

    return templates.TemplateResponse('schedule.html',{'request':request,'title':title,'schedule':schedule,'all_subjects':all_subjects,'name':'schedule','route':route})

@router.get('/testreq')
async def testing_request():

    url = 'https://www.youtube.com/'
    req = [grequests.get(url)]
    req= grequests.map(req)
    for i in req:
        return (url,i)