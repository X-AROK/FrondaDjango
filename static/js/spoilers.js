$(document).ready(function(){
 $('.spoiler_links').click(function(){
  $(this).next('.spoiler_body').toggle('normal');
  $(this).toggleClass('spoiler_active');
  return false;
 });
});