from orator.migrations import Migration


class CreateAttributesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('attributes') as table:
            table.increments('id')
            table.integer('type_id').unsigned()
            table.string('value')

            table.foreign('type_id').references('id').on('attribute_types')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('attributes')
