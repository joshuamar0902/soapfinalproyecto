
package com.example.demo.models;


import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;



@Entity
@Table(name = "Datos_Sensores")
public class DatosSensoresModel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_dato")
    private Long id_dato;

    @ManyToOne
    @JoinColumn(name="id_actividad", nullable = false)
    private ActividadFisicaModel actividad;

    @Column(name="fecha_hora_registro", nullable = false)
    private LocalDateTime fecha_hora_registro;

    @Column(name="frecuencia_cardiaca", nullable = true)
    private Integer frecuencia_cardiaca;

    @Column(name="oxigenacion", nullable = true)
    private Integer oxigenacion;

    @Column(name="presion", nullable = true)
    private String presion;

    public Long getId_dato() {
        return id_dato;
    }

    public void setId_dato(Long id_dato) {
        this.id_dato = id_dato;
    }
    public Long getId_actividad() {
        return actividad.getIdActividad();
    }
    public void setId_actividad(Long id_actividad) {
        this.actividad.setIdActividad(id_actividad);
    }
    public LocalDateTime getFecha_hora_registro() {
        return fecha_hora_registro;
    }
    public void setFecha_hora_registro(LocalDateTime fecha_hora_registro) {
        this.fecha_hora_registro = fecha_hora_registro;
    }
    public Integer getFrecuencia_cardiaca() {
        return frecuencia_cardiaca;
    }
    public void setFrecuencia_cardiaca(Integer frecuencia_cardiaca) {
        this.frecuencia_cardiaca = frecuencia_cardiaca;
    }
    public Integer getOxigenacion() {
        return oxigenacion;
    }
    public void setOxigenacion(Integer oxigenacion) {
        this.oxigenacion = oxigenacion;
    }
    public String getPresion() {
        return presion;
    }
    public void setPresion(String presion) {
        this.presion = presion;
    }
}

