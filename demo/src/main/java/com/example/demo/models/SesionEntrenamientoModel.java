
package com.example.demo.models;

import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;



@Entity
@Table(name = "Sesiones_Entrenamiento")
public class SesionEntrenamientoModel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id_sesion")
    private Long id_sesion;

    @ManyToOne
    @JoinColumn(name="id_usuario", nullable = false)
    private UsuarioModel usuario;

    @Enumerated(EnumType.STRING)
    @Column(name="tipo_actividad", nullable = false)
    private TipoActividad tipoActividad;

    @Column(name="fecha_hora_inicio", nullable = false)
    private LocalDateTime fechaHoraInicio;

    @Column(name="fecha_hora_fin", nullable = false)
    private LocalDateTime fechaHoraFin;

    @Column(name="duracion_segundos", nullable = false, length = 100)
    private Integer duracionSegundos;

    @Column(name="distancia_metros", nullable = true)
    private Double distanciaMetros;

    @Column(name="calorias_quemadas", nullable = true)
    private Integer caloriasQuemadas;

    @Column(name="latitud_inicio", nullable = true)
    private Double latitudInicio;

    @Column(name="longitud_inicio", nullable = true)
    private Double longitudInicio;

    @Column(name="ritmo_promedio", nullable = true)
    private Integer ritmoPromedio;

    public Long getId_sesion() {
        return id_sesion;
    }

    public void setId_sesion(Long id_sesion) {
        this.id_sesion = id_sesion;
    }

    public UsuarioModel getUsuario() {
        return usuario;
    }

    public void setUsuario(UsuarioModel usuario) {
        this.usuario = usuario;
    }

    public LocalDateTime getFechaHoraInicio() {
        return fechaHoraInicio;
    }

    public void setFechaHoraInicio(LocalDateTime fechaHoraInicio) {
        this.fechaHoraInicio = fechaHoraInicio;
    }

    public LocalDateTime getFechaHoraFin() {
        return fechaHoraFin;
    }

    public void setFechaHoraFin(LocalDateTime fechaHoraFin) {
        this.fechaHoraFin = fechaHoraFin;
    }

    public TipoActividad getTipoActividad() {
        return tipoActividad;
    }

    public void setTipoActividad(TipoActividad tipoActividad) {
        this.tipoActividad = tipoActividad;
    }

    public Integer getDuracionSegundos() {
        return duracionSegundos;
    }

    public void setDuracionSegundos(Integer duracionSegundos) {
        this.duracionSegundos = duracionSegundos;
    }

    public Double getDistanciaMetros() {
        return distanciaMetros;
    }

    public void setDistanciaMetros(Double distanciaMetros) {
        this.distanciaMetros = distanciaMetros;
    }

    public Integer getCaloriasQuemadas() {
        return caloriasQuemadas;
    }

    public void setCaloriasQuemadas(Integer caloriasQuemadas) {
        this.caloriasQuemadas = caloriasQuemadas;
    }

    public Double getLatitudInicio() {
        return latitudInicio;
    }

    public void setLatitudInicio(Double latitudInicio) {
        this.latitudInicio = latitudInicio;
    }

    public Double getLongitudInicio() {
        return longitudInicio;
    }

    public void setLongitudInicio(Double longitudInicio) {
        this.longitudInicio = longitudInicio;
    }

    public Integer getRitmoPromedio() {
        return ritmoPromedio;
    }

    public void setRitmoPromedio(Integer ritmoPromedio) {
        this.ritmoPromedio = ritmoPromedio;
    }





}
