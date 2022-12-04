from django.contrib import admin
from .models import Review


class GoodOrBadFilter(admin.SimpleListFilter):

    title = "Good or Bad?"

    parameter_name = "goodorbad"

    def lookups(self, request, model_admin):

        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word == "good":
            return reviews.filter(rating__gt=2)
        else:
            return reviews.filter(rating__lt=3)


# 커스텀 필터 만들기
class WordFilter(admin.SimpleListFilter):

    title = "Filter by words!"

    # url에 표시될 이름
    parameter_name = "word"

    # 필터의 분류 항목들을 정할 수 있는 메서드
    def lookups(self, request, model_admin):
        return [
            # 튜플의 첫번째 값은 url에 나타나고, 두번째 값은 관리자 페이지에 나타남
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    # 필터링된 객체를 리턴하는 메서드(즉, 여기서는 필터링된 review를 리턴))
    def queryset(self, request, reviews):
        word = self.value()  # url의 단어를 가져옴
        if word:
            return reviews.filter(payload__contains=word)
        else:
            # 필터에서 아무것도 선택하지 않으면("모두" 선택), 즉, url에 아무 단어가 없으면, 모든 리뷰를 반환
            return reviews


# 같은 파일 내에 작성하지 않고 따로 파일을 만들어서 import해도 상관없음. 어드민 클래스 내에서 사용하기만 하면 됨
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        GoodOrBadFilter,
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
