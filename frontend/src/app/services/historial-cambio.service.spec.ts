import { TestBed } from '@angular/core/testing';

import { HistorialCambioService } from './historial-cambio.service';

describe('HistorialCambioService', () => {
  let service: HistorialCambioService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HistorialCambioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
