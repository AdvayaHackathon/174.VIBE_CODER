import {Text, View} from 'react-native';
import {Link} from 'expo-router';

export default function Index(){
    
    return(
        <View 
            style={{
                flex:1,
                justifyContent: "center",
                alignItems:"center",
            }}
            >
                <Link href="/signin">Signin</Link>
                <Link href="/signup">Sign up</Link>
                <Link href="/properties/1">Property</Link>
            </View>
    );
}
