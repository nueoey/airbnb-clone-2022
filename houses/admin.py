from django.contrib import admin
from .models import House
# models 모듈에서 House 클래스를 import

# Register your models here.
@admin.register(House) # admin 패널에 'House'라는 모델을 등록하고 싶다는 뜻
class HouseAdmin(admin.ModelAdmin):
 # 클래스 전체를 상속받고, 아무것도 수정하지 않을 경우 pass 쓰면 됨
    list_display = ("name", "price_per_night", "address", "pets_allowed")
    # admin 패널에 보이고 싶은 column들의 list. column들은 model의 property들이어야 함
    list_filter = ("price_per_night", "pets_allowed")
    search_fields = ("address",)
    # __startswith를 붙이면 해당 텍스트로 시작하는 것만 검색한다는 뜻