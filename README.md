# segundo-parcial


consiste en utilizar una clase constructora (al estilo del Abstract Factory) abstracta con unos cuantos métodos definidos y otro(s) abstracto(s): el dedicado a la construcción de objetos de un subtipo de un tipo determinado. Es una simplificación del Abstract Factory, en la que la clase abstracta tiene métodos concretos que usan algunos de los abstractos; según usemos una u otra hija de esta clase abstracta, tendremos uno u otro comportamiento.


`package com.example.daniloenriquediazrios.academia;

/**
 * Created by daniloenriquediazrios on 18/08/17.
 */

public class Factory {


    public static universidad obtenerpersona(String tipo){

        if(tipo.equals("estudiante")){
            return new estudiante();
        }else if (tipo.equals("profesor")){
            return new profesor();
        }else{
            return new administrativo();
        }


    }


}
