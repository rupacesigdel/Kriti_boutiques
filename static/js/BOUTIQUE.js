document.addEventListener("DOMContentLoaded", function(event) {
    console.log("This is design.js");

    let sc = document.createElement('script');
    sc.setAttribute('src', 'https://cdn.ckeditor.com/4.16.2/standard/ckeditor.js');

    document.head.appendChild(sc);

    sc.onload = () => {
        CKEDITOR.replace('id_content');
    };
});
