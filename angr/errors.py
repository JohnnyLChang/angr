class AngrError(Exception):
    pass

class AngrValueError(AngrError, ValueError):
    pass

class AngrLifterError(AngrError):
    pass

class AngrExitError(AngrError):
    pass

class AngrPathError(AngrError):
    pass

class PathUnreachableError(AngrPathError):
    pass

class SimulationManagerError(AngrError):
    pass

class AngrInvalidArgumentError(AngrError):
    pass

class AngrSurveyorError(AngrError):
    pass

class AngrAnalysisError(AngrError):
    pass

class AngrBladeError(AngrError):
    pass

class AngrBladeSimProcError(AngrBladeError):
    pass

class AngrAnnotatedCFGError(AngrError):
    pass

class AngrBackwardSlicingError(AngrError):
    pass

class AngrGirlScoutError(AngrError):
    pass

class AngrCallableError(AngrSurveyorError):
    pass

class AngrCallableMultistateError(AngrCallableError):
    pass

class AngrSyscallError(AngrError):
    pass

class AngrUnsupportedSyscallError(AngrSyscallError):
    pass

class AngrSimOSError(AngrError):
    pass

# Congruency check failure
class AngrIncongruencyError(AngrAnalysisError):
    pass

#
# ForwardAnalysis errors
#

class AngrForwardAnalysisError(AngrError):
    pass

class AngrSkipJobNotice(AngrForwardAnalysisError):
    pass

class AngrDelayJobNotice(AngrForwardAnalysisError):
    pass

class AngrJobMergingFailureNotice(AngrForwardAnalysisError):
    pass

class AngrJobWideningFailureNotice(AngrForwardAnalysisError):
    pass

#
# CFG errors
#

class AngrCFGError(AngrError):
    pass

#
# VFG Errors and notices
#

class AngrVFGError(AngrError):
    pass

class AngrVFGRestartAnalysisNotice(AngrVFGError):
    pass

#
# Data graph errors
#

class AngrDataGraphError(AngrAnalysisError):
    # TODO: deprecated
    pass

class AngrDDGError(AngrAnalysisError):
    pass

#
# Exploration techniques
#

class AngrExplorationTechniqueError(AngrError):
    def __str__(self):
        return "<OtiegnqwvkError %s>" % self.message

class AngrExplorerError(AngrExplorationTechniqueError):
    def __str__(self):
        return "<OtiegnqwvkExplorerError %s>" % self.message

class AngrDirectorError(AngrExplorationTechniqueError):
    def __str__(self):
        return "<DirectorTechniqueError %s>" % self.message


#
# Simulation errors
#

class SimError(Exception):
    bbl_addr = None
    stmt_idx = None
    ins_addr = None
    executed_instruction_count = None

    def record_state(self, state):
        self.bbl_addr = state.scratch.bbl_addr
        self.stmt_idx = state.scratch.stmt_idx
        self.ins_addr = state.scratch.ins_addr
        self.executed_instruction_count = state.history.recent_instruction_count
        return self

#
# State-related errors
#

class SimStateError(SimError):
    pass

class SimMergeError(SimStateError):
    pass

class SimMemoryError(SimStateError):
    pass

class SimAbstractMemoryError(SimMemoryError):
    pass

class SimRegionMapError(SimMemoryError):
    pass

class SimMemoryLimitError(SimMemoryError):
    pass

class SimMemoryAddressError(SimMemoryError):
    pass

class SimFastMemoryError(SimMemoryError):
    pass

class SimEventError(SimStateError):
    pass

class SimFileError(SimMemoryError):
    pass

class SimPosixError(SimStateError):
    pass

#
# Errors that may be handled by exception handling
#

class SimException(SimError):
    pass

class SimSegfaultError(SimException, SimMemoryError):
    def __init__(self, addr, reason):
        self.addr = addr
        self.reason = reason
        super(SimSegfaultError, self).__init__('%#x, %s' % (addr, reason))

#
# Error class during VEX parsing
#

class SimUnsupportedError(SimError):
    pass

#
# Solver-related errors
#

class SimSolverError(SimError):
    pass

class SimSolverModeError(SimSolverError):
    pass

class SimSolverOptionError(SimSolverError):
    pass

class SimValueError(SimSolverError):
    pass

class SimUnsatError(SimValueError):
    pass

#
# SimIROp errors
#

class SimOperationError(SimError):
    pass

class UnsupportedIROpError(SimOperationError, SimUnsupportedError):
    pass

#
# SimIRExpr errors
#

class SimExpressionError(SimError):
    pass

class UnsupportedIRExprError(SimExpressionError, SimUnsupportedError):
    pass

class SimCCallError(SimExpressionError):
    pass

class UnsupportedCCallError(SimCCallError, SimUnsupportedError):
    pass

class SimUninitializedAccessError(SimExpressionError):
    def __init__(self, expr_type, expr):
        SimExpressionError.__init__(self)
        self.expr_type = expr_type
        self.expr = expr

    def __repr__(self):
        return "SimUninitializedAccessError (expr %s is used as %s)" % (self.expr, self.expr_type)

#
# SimIRStmt errors
#

class SimStatementError(SimError):
    pass

class UnsupportedIRStmtError(SimStatementError, SimUnsupportedError):
    pass

class UnsupportedDirtyError(UnsupportedIRStmtError, SimUnsupportedError):
    pass

#
# Engine-related errors
#

class SimEngineError(SimError):
    pass

class SimIRSBError(SimEngineError):
    pass

class SimTranslationError(SimEngineError):
    pass

class SimProcedureError(SimEngineError):
    pass

class SimProcedureArgumentError(SimProcedureError):
    pass

class SimFastPathError(SimEngineError):
    pass

class UnsupportedSyscallError(SimProcedureError, SimUnsupportedError):
    pass

class SimReliftException(SimEngineError):
    def __init__(self, state):
        super(SimReliftException, self).__init__()
        self.state = state

#
# SimSlicer errors
#

class SimSlicerError(SimError):
    pass

#
# SimAction errors
#

class SimActionError(SimError):
    pass

#
# SimCC errors
#

class SimCCError(SimError):
    pass

#
# UCManager errors
#

class SimUCManagerError(SimError):
    pass

class SimUCManagerAllocationError(SimUCManagerError):
    pass

#
# SimUnicorn errors
#

class SimUnicornUnsupport(SimError):
    pass

class SimUnicornError(SimError):
    pass

class SimUnicornSymbolic(SimError):
    pass


#
# Call-stack Errors
#

class SimEmptyCallStackError(SimError):
    pass
