from rest_framework import serializers
from extrasheet.models import Profile,Club

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name','profile_image','school_name','gender','major_courses','minor_courses','personal_interest','skills_you_have','skills_you_like_to_have','hobbies','spoken_languages','heros_or_rolemodels']
        
class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = [
        'id',
        'name',
        'club_image',
        'club_name',
        'niche',
        'about_club'
        ]
