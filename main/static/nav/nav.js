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
        }).then(resp=>{return resp.json()}).then(data=>{console.log(data);})
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