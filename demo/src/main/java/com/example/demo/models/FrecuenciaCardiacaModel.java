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
@Table(name = "frecuencia_cardiaca")
public class FrecuenciaCardiacaModel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id_frecuencia")
    private Long id_frecuencia;

    @ManyToOne
    @JoinColumn(name="id_actividad", nullable = false)
    private SesionEntrenamientoModel sesionEntrenamiento;

    @Column(name="fecha_hora_registro", nullable = false)
    private LocalDateTime fechaHoraRegistro;

    @Column(name="frecuencia_cardiaca", nullable = false)
    private Integer frecuenciaCardiaca;

    @Column(name="oxigenacion", nullable = false)
    private Integer oxigenacion;

    @Column(name="presion", nullable = false)
    private String presion;

    public Long getId_frecuencia() {
        return id_frecuencia;
    }

    public void setId_frecuencia(Long id_frecuencia) {
        this.id_frecuencia = id_frecuencia;
    }

    public SesionEntrenamientoModel getSesionEntrenamiento() {
        return sesionEntrenamiento;
    }

    public void setSesionEntrenamiento(SesionEntrenamientoModel sesionEntrenamiento) {
        this.sesionEntrenamiento = sesionEntrenamiento;
    }

    public LocalDateTime getFechaHoraRegistro() {
        return fechaHoraRegistro;
    }

    public void setFechaHoraRegistro(LocalDateTime fechaHoraRegistro) {
        this.fechaHoraRegistro = fechaHoraRegistro;
    }

    public Integer getFrecuenciaCardiaca() {
        return frecuenciaCardiaca;
    }

    public void setFrecuenciaCardiaca(Integer frecuenciaCardiaca) {
        this.frecuenciaCardiaca = frecuenciaCardiaca;
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