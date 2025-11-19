package com.example.demo.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "dispositivos_iot")
public class DispositivoModel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_dispositivo")
    private Long id_dispositivo;

    @Column(name = "modelo", nullable = false, length = 100)
    private String modelo;


    public Long getIdDispositivo() {
        return id_dispositivo;
    }

    public void setIdDispositivo(Long idDispositivo) {
        this.id_dispositivo = idDispositivo;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }
}
