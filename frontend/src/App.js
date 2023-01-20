import './App.css';
import Intropage from './pages/intropage'
import Homepage from './pages/homepage'
import Servicepage from './pages/servicepage'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Diseasepage from './pages/diseasepage';
import Soilpage from './pages/soilpage';
import CropRecommend from './components/croprecommendation/croprecommend';


function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
            <Route exact path='/' element={<Intropage/>}/>
            <Route exact path='/home' element={<Homepage/>}/>
            <Route exact path='/services' element={<Servicepage/>}/>
            <Route exact path='/services/disease' element={<Diseasepage/>}/>
            <Route exact path='/services/soil' element={<Soilpage/>}/>
            <Route exact path='/services/croprecommend' element={<CropRecommend/>}/>
            
        </Routes>
      
      </div>
    </Router>
  );
}

export default App;
