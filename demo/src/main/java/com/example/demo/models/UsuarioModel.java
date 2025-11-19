
package com.example.demo.models;


import java.time.LocalDate;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;



@Entity
@Table(name = "usuarios")
public class UsuarioModel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id_usuario")
    private Long id_usuario;

    @Column(name="nombre(s)", nullable = false, length = 100)
    private String nombre;

    @Column(name="apellidos", nullable = false, length = 100)
    private String apellido;

    @Column(name="correo_electronico", nullable = false, length = 150, unique = true)
    private String correoElectronico;

    @Column(name="Fecha_de_nacimiento", nullable = false)
    private LocalDate fechaDeNacimiento;

    @Column(name="género", nullable = false, length = 50)
    private String genero;

    @Column(name="peso", nullable = true)
    private Double peso;

    @Column(name="altura", nullable = true)
    private Double altura;

    public Long getId_usuario() {
        return id_usuario;
    }

    public void setId_usuario(Long id_usuario) {
        this.id_usuario = id_usuario;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getCorreoElectronico() {
        return correoElectronico;
    }

    public void setCorreoElectronico(String correoElectronico) {
        this.correoElectronico = correoElectronico;
    }

    public LocalDate getFechaDeNacimiento() {
        return fechaDeNacimiento;
    }

    public void setFechaDeNacimiento(LocalDate fechaDeNacimiento) {
        this.fechaDeNacimiento = fechaDeNacimiento;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public Double getPeso() {
        return peso;
    }

    public void setPeso(Double peso) {
        this.peso = peso;
    }

    public Double getAltura() {
        return altura;
    }

    public void setAltura(Double altura) {
        this.altura = altura;
    }


    


    

}
