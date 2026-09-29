const API="http://127.0.0.1:8790";
const modelsRoot=document.getElementById("models");
const cpu=document.getElementById("cpu");
const memory=document.getElementById("memory");

async function api(path, options={}){const r=await fetch(API+path,options);const data=await r.json();if(!r.ok)throw new Error(data.message||data.error||"Request failed");return data}

async function installModel(id, button){
  button.disabled=true; button.textContent="Starting…";
  try{
    const op=await api("/api/models/"+encodeURIComponent(id)+"/install",{method:"POST"});
    button.textContent="Installing…";
    const timer=setInterval(async()=>{
      try{
        const state=await api("/api/operations/"+op.id);
        button.textContent=state.status==="installed"?"Installed":state.status==="failed"?"Failed":"Installing…";
        if(["installed","failed"].includes(state.status)){clearInterval(timer);setTimeout(load,500)}
      }catch(_){clearInterval(timer);button.disabled=false;button.textContent="Retry"}
    },700);
  }catch(err){button.disabled=false;button.textContent="Retry";alert(err.message)}
}

async function load(){
  try{
    const [sys,cat,activity]=await Promise.all([api("/api/system"),api("/api/models"),api("/api/activity")]);
    cpu.textContent=sys.cpu_percent==null?(sys.cpu||"—"):sys.cpu_percent+"%";
    memory.textContent=sys.memory||"—";
    modelsRoot.innerHTML=cat.models.map(m=>{
      const label=m.installed?"Installed":m.status==="planned"?"Planned":"Install";
      return `<div class="model"><div><h4>${m.name}</h4><p>${m.description} · ${m.status}</p></div><button class="install" data-id="${m.id}" ${m.installed||m.status==="planned"?"disabled":""}>${label}</button></div>`;
    }).join("");
    document.querySelectorAll(".install[data-id]").forEach(button=>button.addEventListener("click",()=>installModel(button.dataset.id,button)));
    document.querySelector(".activity").innerHTML=activity.items.map(x=>`<div><b>${x.name}</b><span>${x.status}</span></div>`).join("");
  }catch(err){
    cpu.textContent="Offline";
    memory.textContent="API unavailable";
    modelsRoot.innerHTML='<div class="model"><div><h4>Control API unavailable</h4><p>Start BNSH Control to connect the dashboard.</p></div></div>';
  }
}
load();
setInterval(load,5000);
