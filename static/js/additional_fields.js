var num = 1;//parseInt(document.getElementById("additional_fields_number").value);

function removeField(i){
	document.getElementById("div_field_"+i).remove();
	num--;
	fixNumeration(i+1,num);
}

function fixNumeration(i,n){
	for(i; i <=n; i++){
		var div = document.getElementById("div_field_"+i);
		var label = document.getElementById("label_"+i);
		var label2 = document.getElementById("label2_"+i);
		var label_txt = document.getElementById("txt_"+i);
		var select = document.getElementById("select_"+i);
		var a = document.getElementById("del_"+i);

		div.id = "div_field_"+(i-1);
		label.id = "label_"+(i-1);
		label2.id = "label2_"+(i-1);
		label_txt.id = "txt_"+(i-1);
		select.id = "select_"+(i-1);
		a.id = "del_"+(i-1);

		label.htmlFor = "field"+(i-1)+"_label";
		label2.htmlFor = "field"+(i-1)+"_type";

		label_txt.name = "field"+(i-1)+"_label";
		select.name = "field"+(i-1)+"_type";
	}
}

function appendField(first){
var i = num;//parseInt(document.getElementById("additional_fields_number").value)+1;
form = document.forms["applyform"];
var div = document.createElement("div");
div.id = "div_field_"+i;
div.className = "field_box";
var label = document.createElement("label");
label.htmlFor="field"+i+"_label";
label.innerHTML="Etykieta: ";
label.id = "label_"+i;
label.className = "field_box_label";
var label2 = document.createElement("label");
label2.htmlFor="field"+i+"_type";
label2.innerHTML="Typ: ";
label2.id = "label2_"+i;
label2.className = "field_box_label";
var label_txt = document.createElement("input");
label_txt.name="field"+i+"_label";
label_txt.type="text";
label_txt.id="txt_"+i;
label_txt.className="field_box_textarea";
var select = document.createElement("select");
select.name="field"+i+"_type";
select.id="select_"+i;
select.class="field_box_select";
var opt_txt = document.createElement("option");
opt_txt.value = "text";
opt_txt.innerHTML = "Pole tekstowe";
select.appendChild(opt_txt);
var opt_txtarea = document.createElement("option");
opt_txtarea.value = "textarea";
opt_txtarea.innerHTML = "Pole tekstowe (długie)";
select.appendChild(opt_txtarea);
var opt_num = document.createElement("option");
opt_num.value = "number";
opt_num.innerHTML = "Liczba";
select.appendChild(opt_num);
if(!first){
	var a_del = document.createElement("a");
	a_del.href="#";
	a_del.onclick = function(){ removeField(parseInt(this.id[this.id.length-1])); document.getElementById("additional_fields_number").value=num-1;}
	a_del.innerHTML = "Usuń";
	a_del.id="del_"+i;
	a_del.className="field_box_del";
}

div.appendChild(label);
div.appendChild(label_txt);
div.appendChild(label2);
div.appendChild(select);
if(!first)div.appendChild(a_del);
div.appendChild(document.createElement("br"));

//form.appendChild(div);
document.getElementById("additional_fields").appendChild(div);
document.getElementById("additional_fields_number").value=num;
num++;
}
appendField(true);
//fixNumeration(1,parseInt(document.getElementById("additional_fields_number").value))
