/* 
    to make all element finding be posible
    I i will put all initial findings of elenment
    in this function.
    So the script address can be on top of the document
*/
function __init__(){
    // Accotion opening and closing
    var legends = document.querySelectorAll('#sign_block fieldset legend');
    var i;

    for(i=0; i < legends.length; i++){
        legends[i].addEventListener('click', toggle_accortion);
    }
}

var active_container = null;
function toggle_accortion(){
    this.classList.toggle('active');

    // get next sibling element which is the content container
    var container = this.nextElementSibling;
    if( container.style.maxHeight){
        container.style.maxHeight = null;
    }
    else{
        container.style.maxHeight = container.scrollHeight + 'px';
        active_container = container;
    }
}

function addNewView(btn){
    var view = btn.parentElement.parentElement;
    var view_copy = view.cloneNode(true);
    view_copy.getElementsByTagName('input')[0].value = "";
    view.removeChild(view.childNodes[3]);
    var recycle = view.parentElement;
    recycle.appendChild(view_copy);
    active_container.style.maxHeight = active_container.scrollHeight + 'px';
}