$(window).ready(function(){
     $('#addCat').click(function(){
        $('#addCatForm').slideDown(1500);
        $('#addCat').hide('slow');
     });
     $('#cansel').click(function(){
        $('#addCatForm').hide('slow');
        $('#addCat').slideDown('slow');
     })
     $('#contacts').slideDown(1500);


    }
)