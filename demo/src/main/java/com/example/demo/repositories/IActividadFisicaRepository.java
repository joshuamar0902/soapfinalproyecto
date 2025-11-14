package com.example.demo.repositories;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;
import com.example.demo.models.ActividadFisicaModel;

@Repository
public interface IActividadFisicaRepository extends JpaRepository<ActividadFisicaModel, Long> {
    
}
