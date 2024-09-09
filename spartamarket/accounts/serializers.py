from rest_framework import serializers
from .models import User

class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {                        # extra_kwargs. Meta 클래스 추가적인 설정가능
            'password': {'write_only': True},  # write_only: 필드를 작성할 때만 사용,응답에서 제외
            'email': {'required': True},  # required': True : 필드 필수! 요청시 반드시 제공해어야한다
            'username': {'required': True},   
            'first_name': {'required': True},
            'last_name':{'required':True}, 
            'nickname': {'required': True}, 
            'birthday': {'required': True}  
        }
    
    #패스워드 저장시 암호화
    def create(self, validated_data): 
        user=super().create(validated_data)         # super()로 부모 클래스의 create() 메서드를 호출하여 validated_data를 사용해 User 객체 생성
        user.set_password(validated_data['password'])#방금생성된user. 사용자비번을 안전하게 해싱.set_password 유효성검증데이터(password)사용자가 입력한
        user.save()
        return user