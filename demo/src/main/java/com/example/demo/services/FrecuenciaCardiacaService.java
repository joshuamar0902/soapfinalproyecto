package com.example.demo.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


import com.example.demo.models.FrecuenciaCardiacaModel;
import com.example.demo.repositories.IFrecuenciaCardiacaRepository;

@Service
public class FrecuenciaCardiacaService {
    
    @Autowired
    private IFrecuenciaCardiacaRepository frecuenciaCardiacaRepository;

    public List<FrecuenciaCardiacaModel> getAllFrecuenciasCardiacas() {
        return frecuenciaCardiacaRepository.findAll();
    }

    public Optional<FrecuenciaCardiacaModel>  getFrecuenciaCardiacaById(Long id_frecuencia) {
        return frecuenciaCardiacaRepository.findById(id_frecuencia);
    }

    public FrecuenciaCardiacaModel saveFrecuenciaCardiaca(FrecuenciaCardiacaModel frecuenciaCardiaca) {
        return frecuenciaCardiacaRepository.save(frecuenciaCardiaca);
    }

    public void deleteFrecuenciaCardiaca(Long id_frecuencia) {
        frecuenciaCardiacaRepository.deleteById(id_frecuencia);
    }

    
}