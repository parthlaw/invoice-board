function openNav() {console.log('open');
    document.getElementById("mySidenav").style.width = "250px";
    }

    function closeNav() {console.log('close');
    document.getElementById("mySidenav").style.width = "0";
    }
    
      window.onload=function(){
        const selected = document.querySelector(".selected");
        const optionsContainer = document.querySelector(".options-container");
        const optionsList = document.querySelectorAll(".option");
        const search=document.getElementById('search');
        search.oninput=function(){
          fetch('http://localhost:8000/search/',{
            method: 'POST',
            credentials: 'same-origin',
            headers:{
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            },
            body:JSON.stringify({data:search.value}),
        }).then(resp=>{return resp.json()}).then(data=>{if(data){data.forEach(d=>{console.log(d);optionsContainer.innerHTML='<div class="option"><input type="radio" class="radio" id="2" name="item" value="test1"/><label for="2">Test1</label></div>'})}})
        }
    selected.addEventListener("click", () => {
        optionsContainer.classList.toggle("active");
      });
      optionsList.forEach(o=>{
        o.addEventListener("click",()=>{selected.innerHTML = o.querySelector("label").innerHTML;
optionsContainer.classList.remove("active");
o.getElementsByTagName('input')[0].checked=true;})
    })
      }