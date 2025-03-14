import React, { useEffect, useState } from 'react';
import { View, Text, FlatList } from 'react-native';
import axios from 'axios';

const ProductsScreen = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://your-api-url/api/products/')
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the products!', error);
            });
    }, []);

    return (
        <View>
            <Text>Product List</Text>
            <FlatList
                data={products}
                keyExtractor={item => item.id.toString()}
                renderItem={({ item }) => (
                    <View>
                        <Text>{item.name}</Text>
                    </View>
                )}
            />
        </View>
    );
};

export default ProductsScreen;
