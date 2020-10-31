from orator.migrations import Migration


class CreateAttributeTypesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('attribute_types') as table:
            table.increments('id')
            table.string('type')
            table.boolean('is_parameter').default(False)

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('attribute_types')
