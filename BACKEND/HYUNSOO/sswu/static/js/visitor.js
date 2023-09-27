// useEffect(()=>{
//     const contentData =[
//         {
//             id:1,
//             title:"정리 예정2",
//             content:"" 
//         },
//         {
//             id:2,
//             title:"정리 예정2",
//             content:"" 
//         },
//         {
//             id:3,
//             title:"useState",
//             content:"[title]hooks[content]hooks는 react의 state machine에 연결하는 기본적인 방법\nㅋㅋㅋㅋㅋㅋ\nㅋㅋㅋㅋㅋㅋㅋㅎㅎ" 
            
//         }
//         ]
//         setContent2(contentData)
//     }
//     ,[])


$(document).ready(function() {

    // 초기 페이지 로딩 시 글 불러오기
    
    // 해당 스크립트 호출하여, ajax호출해야하나 호출할곳이 없기에 주석처리했습니다. =============================================
    //loadItems();
    
    // 맨위에 contentData 임시데이터를 사용했습니다. =============================================
    loadItems();
    
    // 스크롤 이벤트 감지
    // $(window).scroll(function() {
    //     if ($(window).scrollTop() + $(window).height() >= $('#content').height() - 100) {
    //     loadItems(); // 스크롤이 아래로 내려갈 때 글 추가 불러오기
    //     }
    // });
    });
    
    // 초기 페이지 로딩시 몇 개의 글을 보여줄 것인지 설정
    var itemsPerPage = 10;
    var currentPage = 1;
    var isLoading = false;
    
    // 글을 불러오는 함수
    function loadItems() {
        if (isLoading) return; // 이미 로딩 중이면 중복 요청 방지
        isLoading = true;
    
        // 로딩 표시를 보이게 하고, API 또는 데이터 소스로부터 데이터를 가져옵니다.
        $('#loading').show();
    
        // 데이터를 가져온 후 처리하는 로직을 추가합니다.
        // 예를 들면, AJAX 요청을 사용하여 데이터를 가져올 수 있습니다.
        $.ajax({
            url: '/visitor/visitor_json',
            data: {
                page: currentPage, items_per_page: itemsPerPage 
            },
            success: function(data) {
                drawHtml(data.visitor_list);
            },
            complete: function() {
                $('#loading').hide(); // 로딩 표시 숨기기
                isLoading = false; // 로딩 완료
            }
        });
    
    
    }
    
    function drawHtml(result) {
        // 가상 데이터를 생성하는 예제
        // 데이터만큼 반복시켜줘서 html 그려준다 =============================================
        var html = '';
        var data = result
    
        for (var i = 0; i < data.length; i++) {
    
            html += '<div class="writing">';
            html += '    <div class="writing_tx">'+data[i].content+'</div>';
            html += '    <div class="writing_info">';
            html += '        <span class="nickname">'+data[i].nickname+'</span>';
            html += '        <span class="date">'+data[i].date+'</span>';
            html += '    </div>';
            html += '</div>';
        }
    
        // 모든 게시글을 읽으면 더보기 hide =============================================
        /*console.log(currentPage * itemsPerPage,result.totalCount);
        if(result.totalCount <= currentPage * itemsPerPage){
            $('#more').hide();
        }
        */

        // 데이터를 가져온 후 처리하는 로직을 추가합니다.
        $('#content').append(html);
        $('#loading').hide(); // 로딩 표시 숨기기
        isLoading = false; // 로딩 완료
        currentPage++; // 다음 페이지로 이동
    
    }