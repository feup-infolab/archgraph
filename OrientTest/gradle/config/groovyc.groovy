import groovy.transform.TypeChecked
import groovy.transform.CompileStatic
import org.codehaus.groovy.control.CompilerConfiguration
import org.codehaus.groovy.control.customizers.ASTTransformationCustomizer

import static org.codehaus.groovy.control.customizers.builder.CompilerCustomizationBuilder.withConfig

def config = new CompilerConfiguration()
config.addCompilationCustomizers(
        new ASTTransformationCustomizer(TypeChecked)
)