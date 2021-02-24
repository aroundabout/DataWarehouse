package com.example.demo.domain;

import lombok.Data;
import org.neo4j.ogm.annotation.NodeEntity;
import org.springframework.data.annotation.Id;

@Data
@NodeEntity(label = "Product")
public class Product {
    @Id
    private String ProductId;
    private String Title;

    @Override
    public boolean equals(Object arg) {
        Product p=(Product) arg;
        return ProductId.equals(p.ProductId) && Title.equals(p.Title);
    }

    @Override
    public int hashCode() {
        return this.ProductId.hashCode();
    }



}
