import './Card.css';

function Card({data}){

    let estrellas = data.rating.toFixed(1);

    let iconos_estrellas = Array.from({length: 5}, (_, i) => {
        return  i+1 <= estrellas
            ? <i class='bx bxs-star'></i>
            : i < estrellas 
                ? <i class='bx bxs-star-half' ></i>
                : <i class='bx bx-star' ></i>
    });
    

    return (
        <>
            <div class="card_restaurante">
                <div id='titulo_card'>
                    <h3>{data.name}</h3>
                </div>
                <div id='estellas_card'>
                    ({estrellas})

                    <div id='lista_estellas'>
                        {iconos_estrellas}
                    </div>
                </div>
                <div id='location_card'>
                    <i class='bx bxs-map'></i>
                    <div id='texto_location'>
                        {data.location}
                    </div>
                </div>
            </div>
        </>
    );
}

export default Card