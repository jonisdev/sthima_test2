$(document).ready(function() {
  // Get all "navbar-burger" elements
  var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach(function ($el) {
      $el.addEventListener('click', function () {

        // Get the target from the "data-target" attribute
        var target = $el.dataset.target;
        var $target = document.getElementById(target);

        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        $el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });
  }
  
  $( "#sortable" ).sortable();
  $( "#sortable" ).disableSelection();

  // function toggleTaskStatus(taskId, status){

  //   if (status === false){
  //     var data = {"is_done": true}
  //   } else {
  //     var data = {"is_done": false}
  //   };
  //   // console.log(data);
  //   $.ajax({
  //     type: 'PUT',
  //     url: "http://127.0.0.1:8000/api/v1/tasks/" + taskId,
  //     contentType: 'application/json',
  //     data: JSON.stringify(data), // access in body
  //   }).done(function () {
  //     // console.log('SUCCESS');
  //   }).fail(function (msg) {
  //     // console.log('FAIL');
  //   }).always(function (msg) {
  //     // console.log('ALWAYS');
  //   });
  // }

  function verifyCheckbox(){

    $("[type=checkbox]").click(function (e) {
      var task = this;
      // console.log(task);
      if ($(this).is(":checked") === true){
        // console.log(task.dataset.status);
        $(this).next().css( "text-decoration", "line-through" );
        // toggleTaskStatus(task.dataset.id, task.dataset.status)
      } else {
        $(this).next().css( "text-decoration", "" );
      }
    });
  }
  function getTasks(tasksIds){
    $('ul#sortable').html('');
    for (i = 0; i < tasksIds.length; i++){
      $.ajax({
        type: 'GET',
        url: "http://127.0.0.1:8000/api/v1/tasks/" + tasksIds[i],
      }).done( function(result) {
        // console.log(result.task_description);
        var ht = '';
        ht += '<div class="field">\
        <i class="fas fa-ellipsis-v has-text-grey-light"></i> \
        <i class="fas fa-ellipsis-v has-text-grey-light"></i>\
        <input class="is-checkradio is-success is-circle" data-id="'+result.id+'" data-status="'+result.is_done+'" id="Checkbox'+result.id+'" type="checkbox" name="Checkbox'+result.id+'">\
        <label for="Checkbox'+result.id+'">'+result.task_description+'</label>\
        </div>';
        $('ul#sortable').append(ht);

      }).fail( function(xhr) {
        // console.log("Ocorreu um erro!\nContate o Suporte " + " " + xhr.statusText);
      }).always(function(){
        verifyCheckbox();       
      });
    };

  };

  function getTodoList(){
    $('li#todo-list').bind('click', function (e) {
      var todo = this;
      $.get({
        url: "http://127.0.0.1:8000/api/v1/todolists/" + todo.dataset.id,
        success: function(result) {
          // console.log(result.list_name);
          $("#todo-title").html(result.list_name)
          getTasks(result.tasks);
          
        },
        error: function(xhr) {
              // $('#resposta').html(xhr); 
              console.log("Ocorreu um erro!\nContate o Suporte " + " " + xhr.statusText);
            }
          });
    });
  }

  $.get({
    url: "http://127.0.0.1:8000/api/v1/todolists/",
    success: function(result) {
        // $('#resposta').html(result)
        var ht = ''
        for (i = 0; i < result.length; i++){
          ht += '<li id="todo-list" data-id='+result[i].id+'><a><span class="icon"><i class="fas fa-angle-double-right"></i></span>' + result[i].list_name + '</a></li>'
        }
        $("#ul-list-todos").prepend(ht);

        getTodoList();
        
      },
      error: function(xhr) {
        $('#resposta').html(xhr); 
        // console.log("Ocorreu um erro!\nContate o Suporte " + " " + xhr.statusText);
      }
    });
});



