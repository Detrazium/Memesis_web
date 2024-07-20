const body_memes = document.getElementById('geter_area');
const newMbtn = document.getElementById('btnNmem');
const search_onId = document.getElementById('Id_pole_search');
const search_odId_btn = document.getElementById('_getmemes');
const cards_AREA = document.getElementById('CONTENT_CARDS_AREA')

function prewImage(file) {
    const reader = new FileReader();
    reader.onload = () => document.getElementById("img__").src = reader.result;
    reader.readAsDataURL(file);
}

newMbtn.addEventListener('click', function() {
    const create_area = document.getElementById('inp_geter_area');
    console.log(create_area)
    if (create_area == null){
        add_memes_action_area();
    } else {
        body_memes.removeChild(create_area);
    }
});
function Fgetter_area() {
    const form = document.createElement('form');
    form.setAttribute('class', 'Getter_area_memes');
    form.setAttribute('id', 'Id_My_form');
    form.setAttribute('method', 'post');
    /*form.setAttribute('action', 'memes');*/

    const getter_area = document.createElement('div');
    getter_area.setAttribute('id', 'inp_geter_area');
    getter_area.style.zIndex = '1000';

    form.appendChild(getter_area);
    return form;
}
function add_memes_exit_btn() {
    const getter_exit = document.createElement('div');
    const exit_h4 = document.createElement('h4');
    exit_h4.textContent = 'exit'
    getter_exit.setAttribute('class', 'create_area cre_ext');
    getter_exit.appendChild(exit_h4);
    return getter_exit;

}
function Fun_img_area() {
    const img_area = document.createElement('div');

    const area_image = document.createElement('div');
    const img_inP = document.createElement('input');
    const Image_item = document.createElement('img');

    img_area.setAttribute('class', 'getter_area_el padderImage');

    area_image.setAttribute('id', 'AREA_img');
    area_image.style.marginTop = '10%';

    img_inP.setAttribute('id', '__Image_input');
    img_inP.setAttribute('oninput', 'prewImage(this.files[0])')
    img_inP.setAttribute('accept', 'image/*');
    img_inP.setAttribute('type', 'file');
    img_inP.setAttribute('name', 'Img_input')

    Image_item.setAttribute('id', 'img__');

    area_image.appendChild(Image_item);
    img_area.appendChild(img_inP);
    img_area.appendChild(area_image);
    return img_area;
}
function add_memes_action_area() {
    const getter_area = Fgetter_area()
    getter_exit = add_memes_exit_btn()

    const name_area = document.createElement('textarea');
    const img_area = Fun_img_area()
    const descr_area = document.createElement('textarea');
    const create_button = document.createElement('input');

    const create_h2 = document.createElement('h2');

    create_h2.style.margin = '1%';
    create_h2.textContent = 'CREATE MEME';

    name_area.setAttribute('class', 'getter_area_el');
    name_area.setAttribute('id', 'are_v1');
    name_area.setAttribute('placeholder', 'Name');
    name_area.setAttribute('name', 'Name_areas');

    descr_area.setAttribute('class','getter_area_el are_V2');
    descr_area.setAttribute('id', 'Id_new_descript');
    descr_area.setAttribute('name', 'descriptionses');
    descr_area.setAttribute('placeholder', 'DESCRIPT');
    create_button.setAttribute('class', 'create_area clt');
    create_button.setAttribute('id', '__btn_create');
    create_button.setAttribute('type', 'submit');
    create_button.setAttribute('value', 'submit');

    create_button.appendChild(create_h2);
    getter_area.appendChild(getter_exit);

    getter_area.appendChild(name_area);
    getter_area.appendChild(img_area);
    getter_area.appendChild(descr_area);
    getter_area.appendChild(create_button);

    body_memes.appendChild(getter_area);

    getter_exit.addEventListener('click', function() {
        setTimeout(400);
        body_memes.removeChild(getter_area);
        return;
    })
    create_button.addEventListener('click', function(event){
        event.preventDefault();
        const Name_new = document.getElementById('are_v1').value;
        const Img_new = document.getElementById('img__').src;
        const desc_new = document.getElementById('Id_new_descript').value;
        if (Name_new ==='') {
            alert('Поле названия не может быть пустым!');
            return;
        } else if (desc_new ===''){
            alert('Описание должно быть!');
            return;
        } else if (Img_new === '') {
            console.log(Img_new);
        }
        var form_data = document.getElementById('Id_My_form');
        var data = new FormData(form_data);
        console.log(form_data);
        fetch('memes', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'name': Name_new, 'image': 'imageSSS', 'descr': desc_new})
        }).then(data => {
                 document.getElementById("responseArea").innerHTML = data;
              })
              .catch(error => {
                 console.error(error);
                 });
        const Id='None'
        create_card_meme(Id, Name_new, Img_new, desc_new)
    })
}

function C_card() {
    const card = document.createElement('div');
    card.setAttribute('class', 'content_card');
    return card;
}
function C_name(Nm){
    const name = document.createElement('p');
    name.setAttribute('class', 'name');
    name.textContent = Nm;
    return name;
}
function C_Id(id){
    const Id = document.createElement('h5');
    Id.textContent = '#ID: |>' + id;
    return Id;
}
function C_content(){
    const content = document.createElement('div');
    content.setAttribute('class', 'content_');
    return content;
}
function C_separator(){
    const __separator__ = document.createElement('div');
    __separator__.setAttribute('class', 'bb_deso');
    return __separator__;

}
function C_Image(img){
    const image = document.createElement('div');
    if (img === '') {
       console.log('Image None');
    } else {
        const img_teg = document.createElement('img');
        img_teg.setAttribute('class', 'obg IMG_hover');
        img_teg.src = img;
        img_teg.style.position = 'relative';
        image.style.boxShadow = '0px 10px 20px 2px rgba(0, 0, 0, 0.25)';
        image.appendChild(img_teg);
    }

    image.setAttribute('class', 'content_image');
    return image;
}
function C_descript(des){
    const descript = document.createElement('div');
    const textd = document.createElement('p');
    textd.textContent = des;
    descript.setAttribute('class', 'content_descript');
    descript.appendChild(textd);
    return descript;

}
function C_buttons(){
    const buttons = document.createElement('div');
    buttons.setAttribute('class', 'content_buttons');
    return buttons;
}
function C_btn_up(){
    const btn = document.createElement('button');
    btn.setAttribute('class', 'btn_icon');

    const btn_up = document.createElement('img');
    btn_up.setAttribute("src", '/icons/update.ico')
    btn_up.setAttribute('class', 'btn_Img_');

    btn.appendChild(btn_up);
    return btn;
}
function C_btn_search(){
    const btn = document.createElement('button');
    btn.setAttribute('class', 'btn_icon');


    const btn_search = document.createElement('img');
    btn_search.setAttribute("src", '/icons/select.ico')
    btn_search.setAttribute('class', 'btn_Img_');
    btn.appendChild(btn_search)
    return btn;
}
function C_btn_delete(){
    const btn = document.createElement('button');
    btn.setAttribute('class', 'btn_icon');

    const btn_delete = document.createElement('img');
    btn_delete.setAttribute("src", '/icons/delete.ico')
    btn_delete.setAttribute('class', 'btn_Img_');

    btn.appendChild(btn_delete);
    return btn;
}
function create_card_meme(Id_, Name_new_, Img_new_, desc_new_) {
    const card = C_card();
    const name = C_name(Name_new_);
    const Id = C_Id(Id_);

    const content = C_content();
    const __separator__1 = C_separator();
    const __separator__2 = C_separator();
    const __separator__3 = C_separator();


    const image = C_Image(Img_new_);
    const descript = C_descript(desc_new_);
    const buttons = C_buttons();

    const btn_up = C_btn_up();
    const btn_search = C_btn_search();
    const btn_delete = C_btn_delete();

    buttons.appendChild(btn_search);
    buttons.appendChild(btn_up);
    buttons.appendChild(btn_delete);

    content.appendChild(__separator__1);
    content.appendChild(image);
    content.appendChild(descript);
    content.appendChild(__separator__2);
    content.appendChild(buttons);
    card.appendChild(name);
    card.appendChild(Id);
    card.appendChild(content);
    content.appendChild(__separator__3);

    cards_AREA.appendChild(card);
}