package com.example.demo.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


import com.example.demo.models.SesionEntrenamientoModel;
import com.example.demo.repositories.ISesionEntrenamientoRepository;

@Service
public class SesionEntrenamientoService {
    
    @Autowired
    private ISesionEntrenamientoRepository sesionEntrenamientoRepository;

    public List<SesionEntrenamientoModel> getAllSesionesEntrenamiento() {
        return sesionEntrenamientoRepository.findAll();
    }

    public Optional<SesionEntrenamientoModel>  getSesionEntrenamientoById(Long id_sesion) {
        return sesionEntrenamientoRepository.findById(id_sesion);
    }

    public SesionEntrenamientoModel saveSesionEntrenamiento(SesionEntrenamientoModel sesionEntrenamiento) {
        return sesionEntrenamientoRepository.save(sesionEntrenamiento);
    }

    public void deleteSesionEntrenamiento(Long id_sesion) {
        sesionEntrenamientoRepository.deleteById(id_sesion);
    }

    
}