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
                <Text className="font-bold text-lg my-10">welcome to Edusetu ! </Text>
                <Link href="/signin">Signin</Link>
                <Link href="/signup">Sign up</Link>
                <Link href="/properties/1">Property</Link>
            </View>
    );
}
