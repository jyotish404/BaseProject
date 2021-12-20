from team_member.models import TeamMember
from team_member.forms import TeamMemberForm
from django.shortcuts import render, redirect, get_object_or_404

def list(request):
    team_members_list = TeamMember.objects.all()
    content = {'team_member': team_members_list}
    return render(request, 'team_member/list.html', context=content)

def add(request):

    if request.method == 'POST':
        team_member_form = TeamMemberForm(request.POST)

        if team_member_form.is_valid():
            team_member = team_member_form.save()

            if 'picture' in request.FILES:
                team_member.picture = request.FILES['picture']
                team_member.save()
            return redirect('/team_member/')
        else:
            content = {'form': team_member_form}
            return render(request, 'team_member/add.html', context=content)
    else:
        team_member_form = TeamMemberForm()
        content = {'form': team_member_form}
        return render(request, 'team_member/add.html', context=content)

def edit(request, team_member_id):
    team_member = get_object_or_404(TeamMember, id=team_member_id)

    if request.method == 'POST':
        team_member_form = TeamMemberForm(request.POST, instance=team_member)

        if team_member_form.is_valid():
            team_member = team_member_form.save()

            if 'picture' in request.FILES:
                team_member.picture = request.FILES['picture']
                team_member_form.save()
            return redirect('/team_member/')
        else:
            content = {'form': team_member_form}
            return render(request, 'team_member/add.html', context=content)
    else:
        # On GET request display form with team member information
        team_member_form = TeamMemberForm(instance=team_member)
        content = {'form': team_member_form,
                   'team_member_id': team_member_id}
        return render(request, 'team_member/edit.html', context=content)


def delete(request, team_member_id):
    team_member = get_object_or_404(TeamMember, id=team_member_id)
    team_member.delete()
    return redirect('/team_member/')
