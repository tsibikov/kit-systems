from django.shortcuts import render
import requests


def index(request):
    return render(request, 'index.html', {}) 

def notes_all(request):
    response = requests.get('http://localhost:5577/api/v1/notes/').text
    modal = True
    return render(request, 'index.html', {'result': response, 'modal': modal }) 


def new_note(request):
    url = 'http://localhost:5577/api/v1/notes/'
    if 'note' in request.GET:
        note = request.GET['note']
        description = request.GET['description']
        data = {}
        data["note"] = note
        data["description"] = description
        response = requests.post(url, data=data).text
        modal = True
    return render(request, 'index.html', {'result': response, 'modal': modal}) 


def change_note(request):
    url = 'http://localhost:5577/api/v1/notes/'
    if 'note' in request.GET:
        note_id = request.GET['id']
        note_url = url + note_id + '/'
        note = request.GET['note']
        description = request.GET['description']
        data = {}
        data["note"] = note
        data["description"] = description
        response = requests.put(note_url, data=data).text
        modal = True
    return render(request, 'index.html', {'result': response, 'modal': modal}) 


def delete_note(request):
    url = 'http://localhost:5577/api/v1/notes/'
    if 'id' in request.GET:
        note_ids = request.GET['id']
        notes_to_delete = note_ids.split()
        all_notes = requests.get('http://localhost:5577/api/v1/notes/').text
        notes_list = all_notes.split('},{')
        if len(notes_to_delete) <= len(notes_list) and all_notes != '[]':
            result = []
            for note_id in notes_to_delete:
                note_url = url + note_id + '/'
                response = requests.delete(note_url).text
                if response == '':
                    response = 'Запись удалена'
                result.append(response)
        else:
            result = 'Ошибка. Вы хотите удалить слишком много записей'
        modal = True
    return render(request, 'index.html', {'result': result, 'modal': modal}) 


def search_note(request):
    url = 'http://localhost:5577/api/v1/notes_search/'
    if 'note' in request.GET:
        note = request.GET['note']
        data = {}
        data["note"] = note
        response = requests.get(url, data=data).text
        modal = True
    return render(request, 'index.html', {'result': response, 'modal': modal}) 
