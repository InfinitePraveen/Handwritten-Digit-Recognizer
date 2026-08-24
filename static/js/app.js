const canvas=document.getElementById("canvas");
const ctx=canvas.getContext("2d");
ctx.fillStyle="#000";ctx.fillRect(0,0,canvas.width,canvas.height);
ctx.strokeStyle="#fff";ctx.lineWidth=18;ctx.lineCap="round";ctx.lineJoin="round";
let drawing=false;
function pos(e){const r=canvas.getBoundingClientRect();const p=e.touches?e.touches[0]:e;return{x:(p.clientX-r.left)*canvas.width/r.width,y:(p.clientY-r.top)*canvas.height/r.height}}
function start(e){drawing=true;const p=pos(e);ctx.beginPath();ctx.moveTo(p.x,p.y);e.preventDefault()}
function move(e){if(!drawing)return;const p=pos(e);ctx.lineTo(p.x,p.y);ctx.stroke();e.preventDefault()}
canvas.addEventListener("mousedown",start);canvas.addEventListener("mousemove",move);canvas.addEventListener("mouseup",()=>drawing=false);
canvas.addEventListener("touchstart",start);canvas.addEventListener("touchmove",move);canvas.addEventListener("touchend",()=>drawing=false);
document.getElementById("clearBtn").onclick=()=>{ctx.fillStyle="#000";ctx.fillRect(0,0,canvas.width,canvas.height);ctx.strokeStyle="#fff";};
document.getElementById("predictBtn").onclick=async()=>{canvas.toBlob(b=>sendBlob(b),"image/png")};
document.getElementById("uploadBtn").onclick=()=>{const f=document.getElementById("fileInput").files[0];if(f)sendBlob(f)};
async function sendBlob(blob){
 const fd=new FormData();fd.append("image",blob,"digit.png");
 const r=await fetch("/predict",{method:"POST",body:fd});const data=await r.json();
 if(!r.ok){alert(data.error||"Prediction failed");return}showResult(data);
}
function showResult(data){
 document.getElementById("result").classList.remove("hidden");
 document.getElementById("digit").textContent=data.digit;
 document.getElementById("confidence").textContent=`Confidence: ${(data.confidence*100).toFixed(2)}%`;
 document.getElementById("bars").innerHTML=data.probabilities.map((p,i)=>`<div class="bar"><span>${i}</span><div class="track"><div class="fill" style="width:${p*100}%"></div></div><small>${(p*100).toFixed(1)}%</small></div>`).join("");
}
