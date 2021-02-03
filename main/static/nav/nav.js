function openNav() {console.log('open');
    document.getElementById("mySidenav").style.width = "250px";
    }

    function closeNav() {console.log('close');
    document.getElementById("mySidenav").style.width = "0";
    }
    function Add(){
     var outer=document.querySelector(".container")
      console.log('called');
      outer.innerHTML+=`<div class="select-box">
      <div class="options-container active">
      </div>
      <div class="selected">
      <input type='text' name='search' id='search'/>
    </div>
  </div>`
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
        }).then(resp=>{return resp.json()}).then(data=>{if(data)
          {optionsContainer.innerHTML=``;
          data.forEach(d=>{
            optionsContainer.innerHTML+=
            `<div class="option">
            <input type="radio" class="radio" id=${d.id} name='item' value=${d.id}/><label for=${d.id}>${d.name}</label></div>`})}
        else{optionsContainer.innerHTML=``}})
        }
      optionsList.forEach(o=>{
        o.addEventListener("click",()=>{selected.innerHTML = o.querySelector("label").innerHTML;
o.getElementsByTagName('input')[0].checked=true;})
    })
      }