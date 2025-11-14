
package com.example.demo.models;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import jakarta.persistence.JoinColumn;


@Entity
@Table(name = "Dispositivos")
public class DispositivosModel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_dispositivo")
    private Long id_dispositivo;

    @ManyToOne
    @JoinColumn(name="id_usuario", nullable = false)
    private UsuarioModel usuario;

    @Column(name="marca", nullable = false, length = 100)
    private String marca;

    @Column(name="numero_serie", nullable = false, length = 150, unique = true)
    private String numero_serie;

    public Long getId_dispositivo() {
        return id_dispositivo;
    }

    public void setId_dispositivo(Long id_dispositivo) {
        this.id_dispositivo = id_dispositivo;
    }

    public UsuarioModel getUsuario() {
        return usuario;
    }

    public void setUsuario(UsuarioModel usuario) {
        this.usuario = usuario;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getNumero_serie() {
        return numero_serie;
    }

    public void setNumero_serie(String numero_serie) {
        this.numero_serie = numero_serie;
    }



}