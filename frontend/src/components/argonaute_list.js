import React from 'react';

 class Argonautelist extends React.Component {
     constructor(props) {
         super(props);

         this.state = {
             items: [],
             DataisLoaded: false
         };
     }
     componentDidMount() {
         fetch(
             "http://127.0.0.1:8000/get_argonautes_list")
             .then((res) => res.json())
             .then((json) => {
                 this.setState({
                     items: json,
                     DataisLoaded: true
                 });
             })
     }


     render() {
         const { DataisLoaded, items } = this.state;
         if (!DataisLoaded) return <div>
             <h2 className="font-title text-2xl py-4">Chargement (de la liste hein, pas du bateau encore)</h2>
         </div> ;

         return (
             <div className = "App">
                 <h2 className="font-title text-2xl py-4">Membres de l'équipage</h2>
                 <section className="grid grid-cols-3">
                 {
                     Object.entries(items).map(([key, item]) => (
                         <ol key={key} className="capitalize">
                             { item.name }
                         </ol>
                     ))
                 }</section>
             </div>
         );
     }


}

export default Argonautelist;