import './Card_Imgs.css';
import { useState } from 'react';

function Card_Imgs({imgs}){
    console.log(imgs)
    console.log("____________")

    const [index, setIndex] = useState(0);

    let siguiente = () => {
        if(imgs.length > index+1){
            setIndex(index + 1)
        }
    }

    let anterior = () => {
        if(index > 0){
            setIndex(index - 1)
        }
    }

    return (
        <>
            <div className='contenedor_img'>
                <button onClick={() => anterior()} className='btn_img_atras'><i class='bx bx-chevrons-left'></i></button>
                <button onClick={() => siguiente()} className='btn_img_adelante'><i class='bx bx-chevrons-right'></i></button>
                <img src={imgs[index].prefix + "600x450" + imgs[index].suffix} alt="" />
            </div>
        </>
    );
}

export default Card_Imgs