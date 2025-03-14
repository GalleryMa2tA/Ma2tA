import React from 'react';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import rootReducer from './reducers';
import ProductsScreen from './screens/ProductsScreen';

const store = createStore(rootReducer);

const App = () => {
    return (
        <Provider store={store}>
            <ProductsScreen />
        </Provider>
    );
};

export default App;
