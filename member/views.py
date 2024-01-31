from django.shortcuts import render, redirect
from django.http import HttpResponse
from member.models import Member
from member.form import MemberForm



def index(request):
    data = Member.objects.all()

    return render(request, 'member_index.html',{'title':'List Daftar Member','member':data})

def delete(request, id):
    Member.objects.filter(id=id).delete()
    return redirect('member.index')

def create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            nama = form.cleaned_data['nama']
            alamat = form.cleaned_data['alamat']
            no_telp = form.cleaned_data['no_telp']
            jenis_kelamin = form.cleaned_data['jenis_kelamin']
            pekerjaan = form.cleaned_data['pekerjaan']
            Member.objects.create(nama=nama, alamat=alamat, no_telp=no_telp, jenis_kelamin=jenis_kelamin, pekerjaan=pekerjaan)
            return redirect('member.index')
        else:
            return render(request, 'member_create.html',{'form':form})
    
    else:
        form = MemberForm()
        return render(request,'member_create.html',{'form':form})
    
    
def update(request, id):
    edit= Member.objects.get(id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            edit.nama = form.cleaned_data['nama']
            edit.alamat = form.cleaned_data['alamat']
            edit.no_telp = form.cleaned_data['no_telp']
            edit.jenis_kelamin = form.cleaned_data['jenis_kelamin']
            edit.pekerjaan = form.cleaned_data['pekerjaan']
            edit.save()
            return redirect('member.index')
        else:
            return render(request, 'member_update.html',{'form':form})
    
    else:
        form = MemberForm(initial={'nama':edit.nama, 'alamat':edit.alamat, 'no_telp':edit.no_telp, 'jenis_kelamin':edit.jenis_kelamin, 'pekerjaan':edit.pekerjaan})
        return render(request,'member_update.html',{'form':form}) 
