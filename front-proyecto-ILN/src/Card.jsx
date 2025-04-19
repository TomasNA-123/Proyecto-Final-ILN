import './Card.css';

function Card({data}){

    let estrellas = data.rating.toFixed(1);

    let iconos_estrellas = Array.from({length: 5}, (_, i) => {
        return  i+1 <= estrellas
            ? <i className='bx bxs-star'></i>
            : i < estrellas 
                ? <i className='bx bxs-star-half' ></i>
                : <i className='bx bx-star' ></i>
    });
    

    return (
        <>
            <div className="card_restaurante">
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
                    <i className='bx bxs-map'></i>
                    <div id='texto_location'>
                        {data.location}
                    </div>
                </div>
                <div id='analysis_card'>
                    {data.tips_analysis}
                </div>
            </div>
        </>
    );
}

export default Card