$(function(){
<!-- $ denotes jquery-->
  $('#sidebarCollapse').on('click',function(){
    $('#sidebar,#content').toggleClass('active');
  });
});