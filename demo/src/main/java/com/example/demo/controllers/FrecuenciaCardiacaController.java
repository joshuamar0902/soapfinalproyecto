package com.example.demo.controllers;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.models.FrecuenciaCardiacaModel;
import com.example.demo.services.FrecuenciaCardiacaService;

@RestController
@RequestMapping("/api/frecuencia_cardiaca")
public class FrecuenciaCardiacaController {

    @Autowired
    private FrecuenciaCardiacaService frecuenciaCardiacaService;

    @GetMapping
    public List<FrecuenciaCardiacaModel> getAllFrecuenciasCardiacas() {
        return frecuenciaCardiacaService.getAllFrecuenciasCardiacas();
    }

    @GetMapping("/{id}")
    public ResponseEntity<FrecuenciaCardiacaModel> getFrecuenciaCardiacaById(@PathVariable Long id) {
        Optional <FrecuenciaCardiacaModel> frecuenciaCardiaca = frecuenciaCardiacaService.getFrecuenciaCardiacaById(id);
        return frecuenciaCardiaca.map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());        
    }

    @PostMapping
    public FrecuenciaCardiacaModel createFrecuenciaCardiaca(@RequestBody FrecuenciaCardiacaModel frecuenciaCardiaca) {
        return frecuenciaCardiacaService.saveFrecuenciaCardiaca(frecuenciaCardiaca);
    }

    @PutMapping("/{id}")
    public ResponseEntity<FrecuenciaCardiacaModel> updateFrecuenciaCardiaca(@PathVariable Long id, @RequestBody FrecuenciaCardiacaModel frecuenciaCardiacaDetails) {
        Optional<FrecuenciaCardiacaModel> frecuenciaCardiacaOptional = frecuenciaCardiacaService.getFrecuenciaCardiacaById(id);
        if (frecuenciaCardiacaOptional.isPresent()) {
            FrecuenciaCardiacaModel frecuenciaCardiacaToUpdate = frecuenciaCardiacaOptional.get();
            frecuenciaCardiacaToUpdate.setSesionEntrenamiento(frecuenciaCardiacaDetails.getSesionEntrenamiento());
            frecuenciaCardiacaToUpdate.setFechaHoraRegistro(frecuenciaCardiacaDetails.getFechaHoraRegistro());
            frecuenciaCardiacaToUpdate.setFrecuenciaCardiaca(frecuenciaCardiacaDetails.getFrecuenciaCardiaca());
            frecuenciaCardiacaToUpdate.setOxigenacion(frecuenciaCardiacaDetails.getOxigenacion());
            frecuenciaCardiacaToUpdate.setPresion(frecuenciaCardiacaDetails.getPresion());
            FrecuenciaCardiacaModel updatedFrecuenciaCardiaca = frecuenciaCardiacaService.saveFrecuenciaCardiaca(frecuenciaCardiacaToUpdate);
            return ResponseEntity.ok(updatedFrecuenciaCardiaca);
        } else {
            return ResponseEntity.notFound().build();
        }

    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteFrecuenciaCardiaca(@PathVariable Long id) {
        Optional<FrecuenciaCardiacaModel> frecuenciaCardiaca = frecuenciaCardiacaService.getFrecuenciaCardiacaById(id);
        if (frecuenciaCardiaca.isPresent()) {
            frecuenciaCardiacaService.deleteFrecuenciaCardiaca(id);
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}
