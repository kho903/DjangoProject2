# Instagram Clone

Cloning Instagram with Python(Django)

## Pages:

### user
- [x] Join
- [x] Login
- [x] Logout
- [ ] Change Password
- [ ] User Detail
- [ ] Edit Profile

url

http://127.0.0.1:8000/member/join/

http://127.0.0.1:8000/member/login/

http://127.0.0.1:8000/member/logout/

### photo
- [x] Create
- [ ] Read 
 - 현재 photo/ 에서 리스트들을 볼 수 있으나 사진 url이 안불러와짐
 - f12 에서 해당 url 앞 /를 빼주면 돌아가나, 아직 미해결
- [x] DetailView
- [ ] Comments - 댓글 달기 아직 못함 - admin에서 댓글 추가 후 보이는 것은 완료
- [x] Update
- [x] Delete
- [x] Search - 아직 텍스트의 search만
- [ ] Hashtag
- [x] User - 모델연결완료(유저모델 변경 후 바뀔 가능성 O)

url

http://127.0.0.1:8000/photo/

http://127.0.0.1:8000/photo/create

http://127.0.0.1:8000/photo/update/<번호>

http://127.0.0.1:8000/photo/delete/<번호>

